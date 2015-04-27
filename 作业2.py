defBinarSearch (alist,target )
  low,high =0,Ien(alist)-1
  while low<=high：
  mid=（low+high)/2
  mid_val=alist[mid]
  if mid_val<target：
  low=mid+1
  else ：
  return mid
  return -1
 print BinarySearoh
