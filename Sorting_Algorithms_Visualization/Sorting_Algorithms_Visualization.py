#It will be better if you run it on android phone by using interpreter name Pydroid, you can easily find it out on google playstore.
#It is compatible with phone screen resoultion.

import pygame
import time
import random

pygame.init()
color=0
gameDisplay=pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
#bars that are being shown
def bar(list,fps,name,color):
	for i in range(0,len(list),1):
		if color!=list[i]:
			pygame.draw.rect(gameDisplay,(255,255,255),[14*i,900,10,-15*list[i]])
			
		else:
			pygame.draw.rect(gameDisplay,(255,0,0),[14*i,900,10,-15*list[i]])
	clock.tick(fps)
	
	font=pygame.font.SysFont("comicsansms", 50)
	text = font.render(name+' Sorting',True,(255,0,0))
	
	gameDisplay.blit(text,[180,0])
	
	pygame.display.update()
	gameDisplay.fill((0,0,0))
#from here bogoSort algorithm starts
def bogoSort(list,fps,name,color): 

    n = len(list) 

    while (is_sorted(list,fps,name)== False): 

        shuffle(list,fps,name) 

def is_sorted(list,fps,name): 

    n = len(list) 

    for i in range(0, n-1): 

        if (list[i] > list[i+1] ): 

            return False

    return True

def shuffle(list,fps,name): 

    n = len(list) 

    for i in range (0,n): 

        r = random.randint(0,n-1) 

        list[i], list[r] = list[r], list[i]
        color=list[i]
        bar(list,fps,name,color)


#oddeven sorting startinh
def oddEvenSort(list,fps,name,color):

    isSorted = 0

    while isSorted == 0: 

        isSorted = 1

        temp = 0

        for i in range(1, len(list)-1, 2): 

            if list[i] > list[i+1]: 

                list[i], list[i+1] = list[i+1], list[i] 

                isSorted = 0

                  

        for i in range(0, len(list)-1, 2): 

            if list[i] > list[i+1]: 

                list[i], list[i+1] = list[i+1], list[i] 

                isSorted = 0
                color=list[i+1]
                bar(list,fps,name,color)
    return
#bubble sorting 
def bubbleSort(list,fps,name,color):
    for p in range(len(list)-1,0,-1):
        for i in range(p):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                color=list[i+1]
                bar(list,fps,name,color)
             
def cocktailsort(list,fps,name,color):
    def swap(i, j,list,name,fps):
        list[i], list[j] = list[j], list[i]
 
    upper = len(list) - 1
    lower = 0
 
    no_swap = False
    while (not no_swap and upper - lower > 1):
        no_swap = True
        for j in range(lower, upper):
            if list[j + 1] < list[j]:
                swap(j + 1, j,list,fps,name)
                no_swap = False
        upper = upper - 1
 
        for j in range(upper, lower, -1):
            if list[j - 1] > list[j]:
                swap(j - 1, j,list,fps,name)
                no_swap = False
        lower = lower + 1
        color=list[j+1]
        bar(list,fps,name,color)


#selection sort
def selectionSort(list,fps,name,color):
   for f in range(len(list)-1,0,-1):
       p=0
       for l in range(1,f+1):
           if list[l]>list[p]:
               p = l

       temp = list[f]
       list[f] = list[p]
       list[p] = temp
       color=list[p+1]
       bar(list,fps,name,color)

#insertion sort 
def insertionSort(list,fps,name,color):
   for index in range(1,len(list)):

     currentvalue = list[index]
     position = index

     while position>0 and list[position-1]>currentvalue:
         list[position]=list[position-1]
         position = position-1

     list[position]=currentvalue
     color=list[position+1]
     bar(list,fps,name,color)
#combsort
def combsort(list,fps,name,color):
    def swap(i, j,list,fps,name):
        list[i], list[j] = list[j], list[i]
 
    gap = len(list)
    shrink = 1.3
 
    no_swap = False
    while not no_swap:
        gap = int(gap/shrink)
 
        if gap < 1:
            gap = 1
            no_swap = True
        else:
            no_swap = False
 
        i = 0
        while i + gap < len(list):
            if list[i] > list[i + gap]:
                swap(i, i + gap,list,fps,name)
                no_swap = False
            i = i + 1
            color=list[i]
            bar(list,fps,name,color)
#quick sort
def quickSort(list,fps,name,color):
   quickSortHelper(list,0,len(list)-1,fps,name,color)

def quickSortHelper(list,first,last,fps,name,color):
   if first<last:

       splitpoint = partition(list,first,last,fps,name,color)

       quickSortHelper(list,first,splitpoint-1,fps,name,color)
       quickSortHelper(list,splitpoint+1,last,fps,name,color)


def partition(list,first,last,fps,name,color):
   pivotvalue = list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = list[leftmark]
           list[leftmark] = list[rightmark]
           list[rightmark] = temp

   temp = list[first]
   list[first] = list[rightmark]
   list[rightmark] = temp
   color=list[rightmark]

   bar(list,fps,name,color)
   return rightmark
#merge sort
def mergeSort(list,fps,name,color):
    if len(list)>1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        mergeSort(lefthalf,fps,name,color)
        mergeSort(righthalf,fps,name,color)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            list[k]=righthalf[j]
            j=j+1
            k=k+1
        colour=list[i]
        bar(list,fps,name,color)

gameExit=False
while not gameExit:

	l=[30,45,7,17,50,37,27,18,8,34,38,28,46,3,23,32,13,19,9,41,29,47,25,31,5,42,36,15,1,12,40,21,11,33,43,22,48,2,4,14,24,39,16,44,26,6,35,49,20,10]
	m=[30,45,7,17,50,37,27,18,8,34,38,28,46,3,23,32,13,19,9,41,29,47,25,31,5,42,36,15,1,12,40,21,11,33,43,22,48,2,4,14,24,39,16,44,26,6,35,49,20,10]
	n=[30,45,7,17,50,37,27,18,8,34,38,28,46,3,23,32,13,19,9,41,29,47,25,31,5,42,36,15,1,12,40,21,11,33,43,22,48,2,4,14,24,39,16,44,26,6,35,49,20,10]
	o=[30,45,7,17,50,37,27,18,8,34,38,28,46,3,23,32,13,19,9,41,29,47,25,31,5,42,36,15,1,12,40,21,11,33,43,22,48,2,4,14,24,39,16,44,26,6,35,49,20,10]
	h=[30,45,7,17,50,37,27,18,8,34,38,28,46,3,23,32,13,19,9,41,29,47,25,31,5,42,36,15,1,12,40,21,11,33,43,22,48,2,4,14,24,39,16,44,26,6,35,49,20,10]
	i=[30,45,7,17,50,37,27,18,8,34,38,28,46,3,23,32,13,19,9,41,29,47,25,31,5,42,36,15,1,12,40,21,11,33,43,22,48,2,4,14,24,39,16,44,26,6,35,49,20,10]
	g=[30,45,7,17,50,37,27,18,8,34,38,28,46,3,23,32,13,19,9,41,29,47,25,31,5,42,36,15,1,12,40,21,11,33,43,22,48,2,4,14,24,39,16,44,26,6,35,49,20,10]
	k=[30,45,7,17,50,37,27,18,8,34,38,28,46,3,23,32,13,19,9,41,29,47,25,31,5,42,36,15,1,12,40,21,11,33,43,22,48,2,4,14,24,39,16,44,26,6,35,49,20,10]
	j=[30,45,7,17,50,37,27,18,8,34,38,28,46,3,23,32,13,19,9,41,29,47,25,31,5,42,36,15,1,12,40,21,11,33,43,22,48,2,4,14,24,39,16,44,26,6,35,49,20,10]
	p=[3,5,2,1]
	
	bogoSort(p,100,'Bogo',color)
	oddEvenSort(n,40,'Odd Even',color)
	combsort(m,30,'Comb',color)
	bubbleSort(l,30,'Bubble',color)
	cocktailsort(k,19,'Cocktail Shaker',color)
	selectionSort(g,10,'Selection',color)		
	insertionSort(h,30,'Insertion',color)
	quickSort(i,5,'Quick',color)
	mergeSort(j,30,'Merge',color)
	time.sleep(50)
	quit()
