import math
import numpy as np

# Function for denormalization joint coordinates
def denormalization(hand, hand_joint_num, img_height, img_width):
    normalized_x = hand.landmark[hand_joint_num].x
    normalized_y = hand.landmark[hand_joint_num].y
    denorm_x = int(min(math.floor(normalized_x * img_width), img_width - 1))
    denorm_y = int(min(math.floor(normalized_y * img_height), img_height - 1))

    return (denorm_x, denorm_y)

def add_to_list(coord_list, hand):
    if coord_list.shape[0] < 10:        
        coord_list = np.append(coord_list, [[hand.landmark[8].x, hand.landmark[8].y]], axis=0)
                                 
    else:                              
        coord_list = np.delete(coord_list, 0, axis= 0)
        coord_list = np.append(coord_list, [[hand.landmark[8].x, hand.landmark[8].y]], axis=0)        

    return coord_list   
     
def check_mean(coord_list):    
        coord_mean = np.mean(coord_list, axis=0)
        print(f"Mean: {coord_mean}")
        # print(f"Mean value: {coord_mean}"    
        if abs(coord_mean[0] - coord_list[coord_list.shape[0]-1][0]) <= 1 and abs(coord_mean[1] - coord_list[coord_list.shape[0]-1][1]) <= 1:
            point = np.array([coord_mean[0], coord_mean[1]])
            print(f"Point type: {type(point)}")
            return point
    