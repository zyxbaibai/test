# -*- coding: utf-8 -*-


list_1 = [4,5,6,7,2,3,6,9,2]
list_1_sort = sorted(list_1)      # 排序后的列表赋值 不改变原有列表顺序
print('list_1',list_1)            # [4, 5, 6, 7, 2, 3, 6, 9, 2]
print('list_1_sort',list_1_sort)  # [2, 2, 3, 4, 5, 6, 6, 7, 9]
list_1.sort()              # 对原数组排序 不可以赋值给其他变量 否则其他变量为none
print('list_1',list_1)            # [2, 2, 3, 4, 5, 6, 6, 7, 9]

"""
1.插入排序：插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，
从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序；
首先将第一个作为已经排好序的，然后每次从后的取出插入到前面并排序
时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：稳定
"""
def insert_sort(insert_list):
    for i in range(len(insert_list)):
        for j in range(i):
            if insert_list[i] < insert_list[j]:
                insert_list.insert(j,insert_list.pop(i))
                break
    return insert_list
insert_list = insert_sort([4,5,6,7,2,3,6,9,2])
print('插入排序',insert_list)



"""
2.希尔排序：希尔排序是把记录按下标的一定增量分组，
对每组使用直接插入排序算法排序；随着增量逐渐减少，
每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止
时间复杂度：O(n)
空间复杂度：O(n√n)
稳定性：不稳定
"""
def shell_sort(shell_list):
    gap = len(shell_list)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(shell_list)):
            for j in range(i % gap, i, gap):
                if shell_list[i] < shell_list[j]:
                    shell_list[i], shell_list[j] = shell_list[j],shell_list[i]
    return shell_list
shell_list = shell_sort([4,5,6,7,2,3,6,9,2])
# print('希尔排序',shell_list)



"""
3.冒泡排序：它重复地走访过要排序的数列，一次比较两个元素，
如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，
也就是说该数列已经排序完成
时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：稳定
"""
def bubble_sort(bubble_list):
    count = len(bubble_list)
    for i in range(0,count):
        for j in range(i + 1, count):
            if bubble_list[i] > bubble_list[j]:
                bubble_list[i],bubble_list[j] = bubble_list[j], bubble_list[i]
    return bubble_list

bubble_list = bubble_sort([4,5,6,7,2,3,6,9,2])
# print('冒泡排序',bubble_list)



"""
4.快速排序：通过一趟排序将要排序的数据分割成独立的两部分，
其中一部分的所有数据都比另外一部分的所有数据都要小，
然后再按此方法对这两部分数据分别进行快速排序，
整个排序过程可以递归进行，以此达到整个数据变成有序序列
时间复杂度：O(nlog₂n)
空间复杂度：O(nlog₂n)
稳定性：不稳定
"""
def quick_sort(quick_list):
    if quick_list == []:
        return []
    else:
        quick_first = quick_list[0]
        quick_less = quick_sort([l for l in quick_list[1:] if l < quick_first])
        quick_more = quick_sort([m for m in quick_list[1:] if m >= quick_first])
        return quick_less + [quick_first] + quick_more

quick_list = quick_sort([4,5,6,7,2,3,6,9,2])
print('快速排序',quick_list)



"""
5.选择排序：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，
将它与r1交换；第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，
将它与r2交换；以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，
将它与r[i]交换，使有序序列不断增长直到全部排序完毕
时间复杂度：O(n²)
空间复杂度：O(1)
稳定性：不稳定
"""
def select_sort(select_list):
    for i in range(len(select_list)):
        x = i
        for j in range(i, len(select_list)):
            if select_list[j] < select_list[x]:
                x = j
        select_list[i], select_list[x] = select_list[x], select_list[i]
    return select_list
select_list = select_sort([4,5,6,7,2,3,6,9,2])
# print('选择排序',select_list)




"""
6.堆排序：它是选择排序的一种。可以利用数组的特点快速定位指定索引的元素。
堆分为大根堆和小根堆，是完全二叉树。大根堆的要求是每个节点的值都不大于其父节点的值，
即A[PARENT[i]] >= A[i]。在数组的非降序排序中，需要使用的就是大根堆，
因为根据大根堆的要求可知，最大的值一定在堆顶
时间复杂度：O(nlog₂n)
空间复杂度：O(1)
稳定性：不稳定
"""
import copy
def heap_sort(heap_list):
    def heap_adjust(parent):
        child = 2 * parent + 1       # left child
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child + 1] > heap[child]:
                    child += 1       # right child
            if heap[parent] >= heap[child]:
                break
            heap[parent],heap[child] = heap[child], heap[parent]
            parent, child = child, 2 * child + 1

    heap, heap_list = copy.copy(heap_list), []
    for i in range(len(heap) // 2, -1 ,-1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        heap_list.insert(0, heap.pop())
        heap_adjust(0)
    return heap_list

heap_list = heap_sort([4,5,6,7,2,3,6,9,2])
# print('堆排序',heap_list)




"""
7.基数排序：透过键值的部份资讯，将要排序的元素分配至某些“桶”中，藉以达到排序的作用
时间复杂度：O(d(r+n))
空间复杂度：O(rd+n)
稳定性：稳定
"""
def radix_sort(array):
    bucket, digit = [[]], 0
    while len(bucket[0]) != len(array):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        for i in range(len(array)):
            num = (array[i] // 10 ** digit) % 10
            bucket[num].append(array[i])
        array.clear()
        for i in range(len(bucket)):
            array += bucket[i]
        digit += 1
    return array
array = radix_sort([4,5,6,7,2,3,6,9,2])
# print('基数排序',array)






"""
8.归并排序：采用分治法（Divide and Conquer）
的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；
即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，
称为二路归并
时间复杂度：O(nlog₂n)
空间复杂度：O(1)
稳定性：稳定
"""
def merge_sort(array):
    def merge_arr(arr_1, arr_r):
        array = []
        while len(arr_1) and len(arr_r):
            if arr_1[0] <= arr_r[0]:
                array.append(arr_1.pop(0))
            elif arr_1[0] > arr_r[0]:
                array.append(arr_r.pop(0))
        if len(arr_1) != 0:
            array += arr_1
        elif len(arr_r) != 0:
            array += arr_r
        return array

    def recursive(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        arr_1 = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return merge_arr(arr_1, arr_r)
    return recursive(array)

array2 = merge_sort([4,5,6,7,2,3,6,9,2])
# print('归并排序',array2)












