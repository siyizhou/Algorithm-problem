# 冒泡排序
将待排序的元素看作竖着排列的气泡，较小的元素比较轻，从而要往上浮<br>
先比较相邻的元素，如果前一个比后一个大，就交换这两个数；<br>
对每一对相邻的数做相同的操作，从开始到结尾，最后的元素会是最大的数<br>
除去最后一个，针对所有的元素再重复以上步骤，直到没有任何一对数字进行比较<br>

冒泡排序的实现不考虑序列是否已经排好序<br>
冒泡算法的比较次数为（n-i）的加和，其中i从1到n-1<br>
所以执行效率为O(n2)<br>


# 选择排序
基本思想：对待排序的的记录序列进行n-1遍的处理，第i遍的处理是将A[i,n]中最小者与A[i]交换位置<br>
直接选择算法的关键字比较次数与对象的初始排序无关，第i遍选择的最小值对象，需要比较次数为n-i-1<br>
因此总的比较次数为（n-i-1）的加和，其中i从0到n-2<br>
因此，直接选择算法的时间性能为O(n2)<br>


# 插入序列
直接插入排序的基本思想是当插入第i个对象时，前面的A[0]，...，A[i-1]已经排好序<br>
这时，用A[i]与关键字A[i-1],A[i-2]..的关键字顺序进行比较<br>
插入位置即将A[i]插入，原来位置上的对象向后移<br>

在最坏的情况下，第i遍时第i个对象要和前面的i个对象都做关键字比较<br>
并且每做一次就要做一次数据移动<br>
则总的关键字比较次数以及和对象的移动次数分别为<br>
i的加和，其中i从1到n-1，约等于n2/2<br>
i+2的加和，其中i从1到n-1，约等于n2/2<br>
因此插入排序的时间性能为O(n2)<br>
最坏的情况下，复杂度为O(n2)<br>
最好的情况下，复杂度为O(n)<br>

# 归并排序
核心思想：分治<br>
https://blog.csdn.net/k_koris/article/details/80508543<br>
python实现:<br>
https://www.cnblogs.com/Lin-Yi/p/7309143.html<br>

时间复杂度： 最好最坏都是 O(nlogn)<br>
稳定性：稳定<br>
缺点：每次拆分数组都要开心的数组， 每次合并数组都要开新数组，空间复杂度很大<br>

归并细节：比如有两个已经排序好的数组，如何将他归并成一个数组？<br>

我们可以开辟一个临时数组来辅助我们的归并。<br>
也就是说他比我们插入排序也好，选择排序也好多使用了存储的空间，也就是说他需要o（n）的额外空间来完成这个排序。<br>
只不过现在计算机中时间的效率要比空间的效率重要的多。无论是内存也好还是硬盘也好可以存储的数据越来越多，所以设计一个算法，时间复杂度是要优先考虑的。<br>
