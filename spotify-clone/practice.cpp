#include <iostream>
using namespace std;

void countsort(int arr[],int n){
    int largest=-1;
    for (int i = 0; i < n; i++)
    {
        largest=max(largest,arr[i]);
    }
    
    vector<int> count(largest+1,0);
    for (int i = 0; i <n; i++)
    {
        count[arr[i]]++;
    }
    int j=0;
    for (int i = 0; i <=largest; i++)
    {
       while (count[i]!=0)
       {
            arr[j]=i;
            count[i]--;
            j++;
       }
       
    }
    
    return;
    
    
}   


int main(){
    int arr[]={10,2,0,14,20};
    int n=sizeof(arr)/sizeof(int);
    countsort(arr,n);
    for (int i = 0; i < n; i++)
    {
    cout<<arr[i]<<",";
    }
}
