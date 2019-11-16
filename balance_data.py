import numpy as np
import pandas as pd
from collections import  Counter
from random import shuffle
import cv2

train_data = np.load('training_data_1.npy', allow_pickle=True)
print(len(train_data))
df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
right = []
forwards = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]
    if choice == [1,0,0]:
        lefts.append([img, choice])
    elif choice ==[0,1,0]:
        forwards.append([img, choice])
    elif choice == [0,0,1]:
        right.append([img, choice])
    else:
        print('no matches!!!!!')

forwards = forwards[:len(lefts)][:len(right)]
lefts = forwards[:len(forwards)]
right = forwards[:len(forwards)]

final_data = forwards + lefts + right

shuffle(final_data)
print(len(final_data))
np.save('training_data_v2.npy', final_data, allow_pickle=True)




# for data in train_data:
#     img = data[0]
#     choice = data[1]
#     cv2.imshow('test', img)
#     print(choice)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
