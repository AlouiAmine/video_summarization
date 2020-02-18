import h5py
h5_file2 = h5py.File("cognimuse_dataset_merged.h5", 'w')

# h5_file = h5py.File("cognimuse_dataset.h5", 'r')
# h5_file1 = h5py.File("datasets/AR-Tokyo.h5", 'r')
# ls=list(h5_file.keys())+list(h5_file1.keys())
for i in range(1,9):
    h5_file2.create_group('video_{}'.format(i))
file=['cognimuse_dataset.h5','datasets/AR-Tokyo.h5','datasets/CRA.h5','datasets/DEP.h5','datasets/FNE.h5','datasets/GLA.h5']
i=0
for j in range(len(file)):
    filename=file[j]
    dataset = h5py.File(filename, 'r')
    print(filename)
    print(j)
    print()
    for k in range(1,len(list(dataset.keys()))+1):
        i+=1
        print(i)
        print(k)
        h5_file2['video_{}'.format(i)]['features'] = dataset['video_{}'.format(k)]['features'][...]
        h5_file2['video_{}'.format(i)]['picks'] = dataset['video_{}'.format(k)]['picks'][...]
        h5_file2['video_{}'.format(i)]['n_frames'] = dataset['video_{}'.format(k)]['n_frames'][...]
        h5_file2['video_{}'.format(i)]['fps'] = dataset['video_{}'.format(k)]['fps'][...]
        h5_file2['video_{}'.format(i)]['change_points'] = dataset['video_{}'.format(k)]['change_points'][...][...]
        h5_file2['video_{}'.format(i)]['n_frame_per_seg'] = dataset['video_{}'.format(k)]['n_frame_per_seg'][...]
h5_file2.close()