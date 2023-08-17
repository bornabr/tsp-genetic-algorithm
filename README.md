# TSP Problem with Genetic Algorithm
## Data
The input of this problem files with `tsp` format. I used the `tsplib95` library for weighted test cases (`bayg29`) and a self-written loader for test cases with coordinations.

## Algorithm
At first, we generate our initial population with random routes(permutations).

The main process is a loop with several sections. At the end of every iteration in this loop, a new generation is born, preferably with better individuals.

Here is each section of this process:

### Selection
The first thing we do with the previous generation is to select a subset of them as our parents. The primary consideration here is to make a balance between elites and vulgar to prevent overfitting or underfitting.

The algorithm used for this matter is tournament selection. For this, we choose a subset of the population by random, then we sort them based on their fitness and select a number of them as parents.

### Breeding
With the parents being chosen, it is time for mating them with each other. Two individuals create a child with ordered recombination.

For choosing each pair, we shuffle parents and mate them by random. We repeat this shuffling until the number of our children has reached the population size.

### Mutation
We have a parameter called the `mutation_rate`, which specifies the probability of mutation.

The mutations in this problem are done by swapping two cities(genes) in a permutation.

### Replacement
The final step in the loop is to specify the next generation. We have considered a mix of children and parents because we want to keep the best parents for the next generation.
We replace a fixed number of worst children with the best parents.

## Test
### bayg29
My best distances were between 1600 to 1800 and here is one of them:
```
...
Epoch 991 :     Population total fitness: 0.05350538840425015   Best fitness: 0.0006246096189881324     Least Distance: 1601
Epoch 992 :     Population total fitness: 0.05153187693896048   Best fitness: 0.0006246096189881324     Least Distance: 1601
Epoch 993 :     Population total fitness: 0.0513204579709456    Best fitness: 0.0006246096189881324     Least Distance: 1601
Epoch 994 :     Population total fitness: 0.05321649952174588   Best fitness: 0.0006246096189881324     Least Distance: 1601
Epoch 995 :     Population total fitness: 0.05231668309102672   Best fitness: 0.0006246096189881324     Least Distance: 1601
Epoch 996 :     Population total fitness: 0.05274635334638463   Best fitness: 0.0006246096189881324     Least Distance: 1601
Epoch 997 :     Population total fitness: 0.05151979095462216   Best fitness: 0.0006246096189881324     Least Distance: 1601
Epoch 998 :     Population total fitness: 0.052781884167365414  Best fitness: 0.0006246096189881324     Least Distance: 1601
Epoch 999 :     Population total fitness: 0.05374250485540199   Best fitness: 0.0006246096189881324     Least Distance: 1601
Best Answer:
[3, 29, 26, 2, 21, 5, 9, 6, 12, 28, 1, 24, 8, 27, 23, 7, 25, 16, 13, 19, 11, 14, 18, 17, 22, 15, 4, 10, 20] 1601
```
### gr229
My best answers were between 3000 and 4000
```
...
Epoch 9994 :    Population total fitness: 0.058371068766832894  Best fitness: 0.0003179595952426656     Least Distance: 3145.053695381653
Epoch 9995 :    Population total fitness: 0.05820450710359247   Best fitness: 0.0003170750130676965     Least Distance: 3153.8278287053067
Epoch 9996 :    Population total fitness: 0.05882745516984377   Best fitness: 0.0003230745158136518     Least Distance: 3095.2611581929796
Epoch 9997 :    Population total fitness: 0.05743031673631872   Best fitness: 0.00032518360457428136    Least Distance: 3075.185790222001
Epoch 9998 :    Population total fitness: 0.0579201782542021    Best fitness: 0.0003230745158136518     Least Distance: 3095.2611581929796
Epoch 9999 :    Population total fitness: 0.05790317138406781   Best fitness: 0.00031919124164737586    Least Distance: 3132.918042609523
Best Answer:
[33, 76, 90, 55, 52, 69, 78, 229, 228, 226, 227, 217, 218, 225, 224, 6, 7, 8, 4, 5, 9, 58, 83, 62, 60, 54, 63, 66, 65, 81, 15, 26, 31, 32, 97, 104, 95, 37, 107, 105, 106, 129, 114, 126, 111, 89, 86, 56, 18, 61, 87, 88, 80, 77, 25, 22, 30, 34, 115, 139, 142, 134, 164, 176, 199, 200, 222, 221, 203, 213, 215, 214, 207, 208, 216, 220, 210, 205, 206, 209, 219, 223, 201, 158, 204, 141, 148, 150, 212, 202, 211, 159, 132, 138, 128, 135, 144, 143, 146, 152, 136, 133, 170, 172, 173, 174, 177, 178, 180, 48, 193, 192, 162, 165, 163, 181, 184, 183, 175, 186, 196, 198, 195, 194, 191, 190, 189, 49, 43, 44, 47, 188, 45, 42, 46, 50, 187, 197, 182, 185, 41, 168, 179, 40, 29, 39, 38, 167, 171, 166, 169, 131, 130, 149, 156, 160, 157, 145, 147, 155, 151, 154, 153, 161, 140, 137, 127, 110, 118, 123, 121, 122, 119, 103, 102, 100, 94, 99, 91, 36, 35, 96, 124, 109, 108, 113, 125, 117, 112, 101, 74, 71, 72, 116, 120, 98, 93, 84, 19, 51, 10, 20, 21, 24, 68, 64, 59, 82, 70, 73, 67, 75, 92, 85, 79, 23, 53, 3, 11, 57, 17, 16, 2, 1, 12, 13, 14, 27, 28] 3132.918042609523
```
### pr1002
```
Epoch 994 :     Population total fitness: 9.365163303864219e-05         Best fitness: 4.7515001523768794e-07    Least Distance: 2104598.480334179
Epoch 995 :     Population total fitness: 9.365728714334915e-05         Best fitness: 4.7515001523768794e-07    Least Distance: 2104598.480334179
Epoch 996 :     Population total fitness: 9.371571818317812e-05         Best fitness: 4.7544700271831704e-07    Least Distance: 2103283.8450607695
Epoch 997 :     Population total fitness: 9.384172546501668e-05         Best fitness: 4.76046050957672e-07      Least Distance: 2100637.10850721
Epoch 998 :     Population total fitness: 9.381270942079712e-05         Best fitness: 4.76046050957672e-07      Least Distance: 2100637.10850721
Epoch 999 :     Population total fitness: 9.385056157475118e-05         Best fitness: 4.7627303441693017e-07    Least Distance: 2099635.9813320828
Best Answer:
[473, 387, 379, 643, 359, 652, 354, 28, 321, 401, 399, 299, 276, 122, 154, 216, 220, 204, 226, 258, 318, 121, 259, 150, 300, 268, 245, 478, 471, 488, 513, 582, 574, 467, 506, 500, 486, 472, 554, 606, 627, 375, 437, 287, 281, 317, 323, 39, 329, 427, 464, 477, 446, 442, 396, 400, 383, 111, 123, 33, 99, 127, 93, 102, 157, 156, 170, 167, 254, 181, 192, 191, 217, 501, 532, 874, 858, 832, 847, 814, 836, 1002, 822, 824, 839, 857, 902, 927, 922, 918, 875, 910, 912, 926, 962, 768, 771, 1000, 784, 937, 765, 702, 975, 961, 957, 776, 833, 525, 843, 906, 909, 864, 813, 897, 773, 703, 754, 781, 750, 752, 616, 628, 790, 727, 794, 671, 721, 716, 942, 914, 964, 974, 940, 763, 792, 791, 951, 772, 769, 834, 553, 566, 521, 590, 498, 530, 845, 1001, 806, 789, 959, 685, 343, 360, 44, 7, 9, 58, 65, 45, 91, 47, 430, 344, 368, 394, 235, 197, 207, 263, 484, 200, 509, 201, 232, 438, 339, 661, 326, 74, 1, 11, 8, 2, 3, 37, 348, 640, 402, 385, 364, 410, 352, 358, 357, 620, 630, 453, 609, 734, 767, 934, 770, 952, 968, 774, 748, 766, 936, 742, 731, 376, 378, 380, 407, 365, 664, 384, 346, 646, 795, 835, 863, 895, 919, 759, 821, 537, 512, 508, 494, 482, 474, 483, 222, 238, 205, 172, 173, 280, 432, 429, 451, 431, 21, 87, 94, 179, 161, 196, 234, 203, 510, 195, 246, 565, 825, 810, 899, 865, 848, 842, 885, 944, 947, 696, 735, 393, 351, 347, 398, 107, 112, 282, 97, 96, 148, 132, 128, 103, 84, 320, 113, 186, 188, 507, 996, 250, 242, 149, 120, 298, 293, 307, 290, 614, 998, 492, 502, 524, 450, 411, 10, 16, 991, 134, 98, 327, 332, 19, 333, 73, 71, 312, 315, 31, 285, 138, 118, 257, 309, 295, 604, 629, 686, 617, 634, 753, 965, 985, 709, 701, 969, 695, 720, 679, 669, 691, 715, 726, 694, 981, 737, 744, 741, 967, 955, 984, 956, 933, 928, 860, 534, 533, 548, 829, 557, 552, 823, 569, 523, 859, 905, 881, 921, 923, 887, 820, 838, 869, 815, 538, 546, 578, 479, 275, 251, 237, 228, 469, 470, 288, 46, 51, 271, 270, 249, 223, 163, 174, 155, 239, 187, 233, 153, 144, 79, 76, 54, 493, 584, 555, 830, 527, 595, 819, 900, 743, 979, 747, 456, 426, 225, 264, 324, 22, 40, 41, 61, 25, 311, 314, 34, 50, 391, 648, 651, 977, 712, 707, 697, 711, 954, 693, 960, 841, 930, 886, 856, 878, 890, 884, 924, 883, 861, 851, 870, 888, 802, 939, 920, 904, 786, 704, 972, 687, 689, 668, 371, 373, 611, 625, 367, 419, 405, 422, 623, 334, 27, 24, 26, 297, 38, 110, 90, 151, 209, 485, 517, 559, 576, 545, 873, 849, 850, 898, 862, 872, 880, 803, 764, 779, 605, 586, 487, 598, 876, 915, 760, 698, 692, 717, 724, 725, 706, 377, 105, 133, 101, 49, 366, 345, 341, 645, 997, 445, 403, 52, 70, 53, 330, 301, 43, 319, 92, 221, 212, 182, 504, 499, 468, 260, 496, 189, 248, 194, 164, 116, 230, 491, 505, 183, 190, 224, 168, 262, 273, 457, 440, 106, 310, 67, 313, 64, 20, 406, 418, 641, 389, 656, 622, 655, 374, 415, 417, 409, 304, 13, 62, 316, 283, 601, 599, 520, 597, 531, 219, 540, 889, 853, 831, 855, 844, 893, 854, 879, 978, 688, 732, 412, 465, 447, 274, 256, 202, 198, 213, 490, 272, 414, 413, 420, 56, 12, 328, 18, 296, 408, 382, 421, 289, 277, 137, 81, 89, 75, 69, 5, 59, 60, 306, 135, 100, 136, 247, 518, 999, 208, 206, 243, 236, 211, 229, 269, 265, 162, 165, 159, 160, 145, 331, 416, 423, 458, 454, 185, 210, 591, 561, 796, 690, 980, 663, 678, 713, 963, 699, 986, 966, 982, 749, 746, 990, 673, 987, 675, 667, 719, 728, 612, 603, 444, 495, 587, 585, 631, 639, 388, 392, 338, 708, 700, 662, 337, 650, 619, 644, 635, 637, 624, 626, 618, 665, 740, 943, 714, 973, 799, 710, 681, 935, 777, 705, 983, 683, 676, 970, 594, 558, 840, 929, 896, 907, 827, 571, 522, 551, 535, 600, 941, 762, 949, 989, 684, 672, 670, 356, 381, 294, 353, 362, 390, 349, 336, 369, 370, 372, 395, 291, 428, 476, 596, 549, 547, 615, 636, 579, 516, 231, 169, 171, 240, 227, 108, 267, 255, 147, 129, 104, 180, 177, 193, 503, 528, 818, 556, 461, 436, 462, 463, 758, 745, 613, 610, 733, 718, 958, 953, 755, 782, 797, 828, 593, 592, 266, 141, 125, 529, 515, 575, 778, 738, 756, 804, 761, 757, 751, 441, 588, 570, 475, 581, 572, 567, 519, 809, 775, 780, 911, 892, 871, 916, 908, 901, 812, 807, 793, 785, 868, 913, 817, 837, 816, 550, 800, 787, 801, 562, 573, 826, 543, 563, 536, 811, 877, 948, 950, 677, 976, 932, 846, 852, 867, 903, 866, 425, 481, 489, 526, 560, 448, 449, 577, 539, 541, 511, 241, 252, 995, 214, 215, 514, 589, 608, 434, 459, 404, 325, 32, 15, 30, 35, 23, 68, 117, 115, 114, 284, 218, 124, 994, 66, 17, 72, 83, 14, 48, 340, 363, 292, 36, 55, 82, 77, 158, 244, 455, 439, 424, 435, 602, 805, 788, 633, 992, 642, 355, 335, 29, 397, 658, 657, 654, 682, 739, 971, 722, 659, 621, 730, 798, 783, 680, 666, 723, 660, 342, 361, 653, 729, 736, 386, 674, 945, 988, 946, 993, 938, 925, 882, 917, 931, 891, 894, 808, 542, 583, 452, 632, 607, 433, 580, 544, 564, 568, 497, 184, 199, 261, 466, 278, 303, 302, 139, 80, 4, 63, 42, 130, 131, 119, 86, 146, 88, 109, 308, 305, 279, 6, 57, 443, 480, 143, 152, 142, 126, 253, 166, 178, 175, 176, 78, 140, 95, 85, 460, 286, 322, 638, 350, 649, 647] 2099635.9813320828
```
## Considerations
- Because we want to optimize our answers based on the total distance of the cycle, our fitness function is `1/total_distance` (so we try to maximize fitness).
