
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = {}
    file_list = listdir(image_dir)
    label_list = []
    
    for file in file_list:
        if file[0] != ".":
            file_name = file.lower()
            file_name = file_name[0:file_name.find(".")]
            file_words = file_name.split("_")
            label = ""
            for word in file_words:
                if word.isalpha() == True:
                    label = label + word + " "
            label = label.strip()
            label_list.append(label)
            if file not in results_dic:
                results_dic[file] = [label]
            else:
                print("The following file has already been added: " + file) 
        else: 
            continue

    return results_dic
