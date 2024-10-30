#include <iostream>
#include <fstream>
#include<vector>
#include <set>
#include<algorithm>

using namespace std;


set<int> intersection_sets(const set<int>&A,const set<int>&B)
{
    set<int> result;
    set_intersection(A.begin(),A.end(),B.begin(),B.end(),inserter(result,result.begin()));
    return result;


}
set<int> difference_sets(const set<int>& A,const set<int>& B)
{
    set<int> result;
    set_difference(A.begin(),A.end(),B.begin(),B.end(),inserter(result,result.begin()));
    return result;
}
set<int> union_sets(const set<int>& a,const set<int>& b)
{
    set<int> result;
    set_union(a.begin(),a.end(),b.begin(),b.end(),inserter(result,result.begin()));
    return result;

}
void print_set(const set<int>& abc,const string& set_name)
{
    cout<<set_name<<" : ";
    for(const auto s : abc )
    {
        cout<<s<<" ";
    
    }
    cout<<endl;
}


int main()
{
    
    set<int> dizi1={1,2,3,4,5};
    set<int> dizi2={2,3,4,6,7};
    set<int>birlesim=union_sets(dizi1,dizi2);
    print_set(birlesim,"Birlesim A U B");
    set<int>kesisim=intersection_sets(dizi1,dizi2);
    print_set(kesisim,"A n B : ");
    set<int>fark=difference_sets(dizi1,dizi2);
    print_set(fark,"kesisim : ");
    

}




   



    







