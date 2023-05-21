"""
Forked from SCAN (https://github.com/wvangansbeke/Unsupervised-Classification).
"""
import os

<<<<<<< HEAD
class MyPath(object):
    @staticmethod
    def db_root_dir(database=''):
        db_names = {'cifar-10', 'stl-10', 'cifar-20', 'imagenet', 'imagenet_50', 'imagenet_100', 'imagenet_200'}
        assert(database in db_names)

        if database == 'cifar-10':
            return '/stcai/datasets/public/cifar-10/'
        
        elif database == 'cifar-20':
            return '/path/to/cifar-20/'

        elif database == 'stl-10':
            return '/path/to/stl-10/'
        
        elif database in ['imagenet', 'imagenet_50', 'imagenet_100', 'imagenet_200']:
            return '/path/to/imagenet/'
        
=======

class MyPath(object):
    @staticmethod
    def db_root_dir(database=''):
        db_names = {'cifar-10', 'stl-10'}
        assert(database in db_names)

        if database == 'cifar-10':
            return '/dataset/cifar-10/'
        elif database == 'stl-10':
            return '/dataset/stl-10/'
>>>>>>> 7572dc5671b7a743af4c3aead34299d8b859cca9
        else:
            raise NotImplementedError
