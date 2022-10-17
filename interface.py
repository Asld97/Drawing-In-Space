import math

# Function for denormalization joint coordinates
def denormalization(hand, hand_joint_num, img_height, img_width):
    normalized_x = hand.landmark[hand_joint_num].x 
    normalized_y = hand.landmark[hand_joint_num].y
    denorm_x = int(min(math.floor(normalized_x * img_width), img_width - 1))
    denorm_y = int(min(math.floor(normalized_y * img_height), img_height - 1))

    return (denorm_x, denorm_y)




