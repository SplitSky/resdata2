# this file is used by Jupyter to run commands used in analysis and streamlines the interface
from . import datastructure as d
import matplotlib.pyplot as plt
import numpy as np
import json
import os
from typing import List
from . import testing as t

def plot_from_dataset(dataset : d.Dataset, label: str, title: str):
    # check dimensionality
    dims = len(dataset.data)

    if dataset.data_type in ["dimensions"]:
        # print out dimensions
        for i in range(0,len(dataset.data_headings),1):
            print(str(dataset.data_headings[i]) + " : " + str(dataset.data[i]))
    else:
        # plot out spectra
        if dims == 1:
            # 1D spectrum
            y = dataset.data
            x = np.arange(0,len(y))
            print("printing 1D spectrum")
            plt.xlabel = "number"
            plt.ylabel = dataset.data_headings[0]
            plt.title(title)
            plt.plot(x,y, label=label)
            plt.legend()

        elif dims == 2:
            # 2D plot 
            x,y = dataset.data
            print("printing 2D spectrum")
            plt.xlabel = dataset.data_headings[0]
            plt.ylabel = dataset.data_headings[1]
            plt.title(title)
            plt.plot(x,y, label=label)
            plt.legend()

        elif dims == 3:
            x, y, z = dataset.data
            print("Printing 2D spectrum with error bars")
            plt.xlabel = dataset.data_headings[0]
            plt.ylabel = dataset.data_headings[1]
            plt.plot(x,y)
            plt.title(title)
            plt.errorbar(x,y,z, label=label)
            plt.legend()

        else:
            raise Exception("the dimensionality too high")
        plt.show()

def summarise_dimensions(datasets: list[d.Dataset]):
    # generate the temp variable
    variable_keys = datasets[0].data_headings

    var_temp = []
    for entry in variable_keys:
        var_temp.append([])

    for dataset in datasets:
        for i in range(0,len(dataset.data_headings),1):
            var_temp[i].append(dataset.data[i])

    # calculate means and errors
    print("Average values for dimensions: ")
    i = 0
    for array in var_temp:
        mean = np.array(array).mean()
        std = np.array(array).std()
        print(f"{datasets[0].data_headings[i]} : {mean} +/- {std}")
        i += 1
       
def unpack_h5_custom_proj(json_file_name : str, username: str, project_name : str, experiment_name : str, max_ring_id : int):
    # instead of saving individual datasets saves the data fully into one project

    with open(json_file_name, "r") as file:
        data = file.readlines()
        file.close()
    data = data[0]
    json_data = json.loads(data)
    # NOTE: This data has badly labelled ring_ids. They are non-unique hence they are relabelled

    dimensions_keys = ['ring_ID', 'sample_ID', 'position', 'fluence', 'abs_position', 'thresh_est' ,'threshold', 'lasing_wavelength', 'mode_spacing', 'lasing_spacing_error', 'lasing_amplitude', 'field_ID', 'pos_rot', 'array_ID']
    spectra_keys = ['PL_screen', 'pdep', 'p', 'pint' ,'images', 'wl']
    
    author_temp = [d.Author(name=username, permission="write").dict()]
    experiment = d.Experiment(name=experiment_name, children=[], author=author_temp)
    project = d.Project(name=project_name, creator=username,groups=[],author=author_temp)
    # loop over ring_id and append the variables
    names = []
    print(f'ring_id: {len(json_data.get("ring_ID"))}')

    for key in json_data.keys():
        print(f'{key} : {len(json_data.get(key))}')

    ring_ID = 0
    for entry in json_data.get("ring_ID"):
        # unpack single ring
        print(f'ring_ID: {entry}')
        print(f'new_ring_ID: {ring_ID}')
        data_temp = []
        for heading in dimensions_keys:
            data_temp.append(json_data.get(heading)[ring_ID])
        #sample ID
        temp = json_data.get("sample_ID")
        dataset_temp = d.Dataset(name="ring_id " + str(ring_ID) + " dimensions", data=data_temp, meta={"old_ring_id" : entry, "ring_id" : ring_ID, "sample_id" : temp}, data_type="dimensions",author=author_temp, data_headings=dimensions_keys)
        
        experiment.children.append(dataset_temp) 

        data_headings_temp = []
        data_full = []
        # append the spectra
        for spectrum_name in spectra_keys:
            data_full.append(json_data.get(spectrum_name)[ring_ID])
            data_headings_temp.append(spectrum_name)
        dataset_temp = d.Dataset(name="ring_id " + str(ring_ID) + " - spectra", data=data_full, meta={"old_ring_id" : entry, "ring_id" : ring_ID}, author=author_temp, 
                                     data_headings=data_headings_temp, data_type="spectrum")
        experiment.children.append(dataset_temp)
        ring_ID += 1
        if ring_ID > max_ring_id:
            # wrap the experiment in a project
            project.groups=[experiment]
            t.save_file_project(file_name=project_name+".json", project=project)
            return project_name+".json"

# save datasets unpacked into individual .json files
def save_dataset(dataset_in: d.Dataset):
    filename = dataset_in.name + ".json"
    with open(filename, "w") as f:
        json.dump(dataset_in.convertJSON(), f)
        f.close()
    return filename

def append_name(name: str):
    file_name_temp = "names.txt"
    with open(file_name_temp, "w+") as f:
        f.write(name)
        f.write('\n')
        f.close()

