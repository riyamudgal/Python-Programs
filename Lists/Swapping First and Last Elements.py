def swap(List):
    s=len(List)
      
    temp=List[0]
    List[0]=List[s-1]
    List[s-1]=temp
      
    return List
     
List = [12, 35, 9, 56, 24]
  
result=swap(newList)
print(result)
