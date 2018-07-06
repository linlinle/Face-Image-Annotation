import tensorflow as tf
import numpy as np
import argparse
import os
import cv2
import time
from tensorflow.python.platform import gfile


def main():
    args = parse_arguments()
    with tf.Graph().as_default():
        with tf.Session() as sess:
            
            # Read the file containing the pairs used for testing
            pairs = read_pairs(os.path.expanduser(args.lfw_pairs))
            
            # Get the paths for the corresponding images
            paths, actual_issame = get_paths(os.path.expanduser(args.lfw_dir), pairs, 'jpg')
            
            # load model
            print('Model filename: %s' % args.model)
            with gfile.FastGFile(args.model,'rb') as f:
                graph_def = tf.GraphDef()
                graph_def.ParseFromString(f.read())
                # import graph into session
                tf.import_graph_def(graph_def, name='')
                
            # Get input and output tensors
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            trainable = tf.get_default_graph().get_tensor_by_name("phase_train:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            
            image_size = images_placeholder.get_shape().as_list()[2]
            embedding_size = embeddings.get_shape().as_list()[1]
            
            # Run forward pass to calculate embeddings
            print('Runnning forward pass on LFW images...')
            cos = []
            for i in range(len(paths)):
                images = load_data(paths[i], 112, 96)
                start = time.clock()
                vectors_normed = sess.run(embeddings, feed_dict={images_placeholder:images, trainable:False})
                end = time.clock()
                cos.append(np.dot(vectors_normed[0], vectors_normed[1]))
                print("predict %d/%d, elapse %f"%(i, len(paths), end-start))
            cos = np.array(cos)
            np.save('cos.npy', cos)
 
            cos = np.load('cos.npy')
            # calculate the accuracy on lfw
            print("calculate the accuracy on lfw...")
            thresholds = np.arange(0, 1, 0.01)
            best_threshold = 0
            max_correct = 0
            for threshold in thresholds:
                logits = cos>threshold
                correct = np.sum(np.equal(logits, actual_issame))
                  
                if correct > max_correct:
                    max_correct = correct
                    best_threshold = threshold
            accuracy = max_correct/cos.size
            print("accurary %f"%accuracy)
            print("threshold %f"%best_threshold)
            

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", help="path to model.pb file")
    parser.add_argument("--lfw_dir", help="path to lfw dataset")
    parser.add_argument("--lfw_pairs", help="path to lfw_pairs")
    args = parser.parse_args()
    return args

def read_pairs(pairs_filename):
    pairs = []
    with open(pairs_filename, 'r') as f:
        for line in f.readlines()[1:]:
            pair = line.strip().split()
            pairs.append(pair)
    return np.array(pairs)

def get_paths(lfw_dir, pairs, file_ext):
    nrof_skipped_pairs = 0
    path_list = []
    issame_list = []
    for pair in pairs:
        if len(pair) == 3:
            path0 = os.path.join(lfw_dir, pair[0], pair[0] + '_' + '%04d' % int(pair[1])+'.'+file_ext)
            path1 = os.path.join(lfw_dir, pair[0], pair[0] + '_' + '%04d' % int(pair[2])+'.'+file_ext)
            issame = True
        elif len(pair) == 4:
            path0 = os.path.join(lfw_dir, pair[0], pair[0] + '_' + '%04d' % int(pair[1])+'.'+file_ext)
            path1 = os.path.join(lfw_dir, pair[2], pair[2] + '_' + '%04d' % int(pair[3])+'.'+file_ext)
            issame = False
        if os.path.exists(path0) and os.path.exists(path1):    # Only add the pair if both paths exist
            path_list.append([path0,path1])
            issame_list.append(issame)
        else:
            nrof_skipped_pairs += 1
    if nrof_skipped_pairs>0:
        print('Skipped %d image pairs' % nrof_skipped_pairs)
    
    return path_list, issame_list

def load_data(image_paths, H, W):
    nrof_samples = len(image_paths)
    images = np.zeros((nrof_samples, H, W, 3))
    for i in range(nrof_samples):
        img = cv2.imread(image_paths[i])
        img = cv2.resize(img, (W, H))
        images[i,:,:,:] = img

    return np.array(images)

def load_lfw(image_paths, H, W):
    nrof_samples = len(image_paths)
    images = np.zeros((nrof_samples, H, W, 3))
    for i in range(nrof_samples):
        img = cv2.imread(image_paths[i])
        img = cv2.resize(img, (W, H))
        images[i,:,:,:] = img

    return np.array(images)

if __name__ == '__main__':
    main()