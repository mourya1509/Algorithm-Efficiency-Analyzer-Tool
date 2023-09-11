from sortingAlgorithms import InsertionSort,MergeSort,BubbleSort,HeapSort,BucketSort_090923,CountingSort_090923,QuickSort,RadixSort_090923
import time



class SortInteger:

       
    #function to sort string array
    def SortInteger(UnSortedArray,sortMethod):

        #use below sorting algorithms for String Input  
        sortingmethods = {
        "InsertionSort":list(InsertionSort.insertion_sort(UnSortedArray)),
        "BubbleSort":list(BubbleSort.bubble_sort(UnSortedArray)),
        "MergeSort":list(MergeSort.merge_sort(UnSortedArray)),
        "HeapSort":list(HeapSort.heap_sort(UnSortedArray)),
        "BucketSort":list(BucketSort_090923.bucket_sort(UnSortedArray)),
       # "CountingSort":CountingSort_090923.counting_sort(UnSortedArray),
        "QuickSort":list(QuickSort.quick_sort(UnSortedArray, 0, len(UnSortedArray)-1)),
        "RadixSort":list(RadixSort_090923.radix_sort(UnSortedArray))


        }
        # start timer
        start = time.process_time()
        #sort array using user inputted method
        sortedArray = sortingmethods.get(sortMethod, "nothing")
       
        #end timer
        end = time.process_time()
        return sortedArray,end-start




#replace hardcoded input with the input from  frontend
UnSortedArray =[-5, -3, 2, -8, 1, 6]
print("Unsorted array",UnSortedArray)

sortingmethod =input("Select Sorting Mehtods:  InsertionSort BubbleSort  MergeSort HeapSort BucketSort CountingSort QuickSort RadixSort ")



sortedArray, time_consumed = SortInteger.SortInteger(UnSortedArray,sortingmethod)
print("Time Consumed " ,time_consumed)
print("Sorted array  ",sortedArray,sortingmethod)

# test= InsertionSort.insertion_sort(UnSortedArray)
# print("testttt",test)