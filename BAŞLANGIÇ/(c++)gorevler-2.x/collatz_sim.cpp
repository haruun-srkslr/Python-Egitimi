#include<iostream>
#include<vector>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std;

vector<int> collatz_sim(int n)
{
    int new_num;
    vector<int> steps;
    while(n!=1)
    {
        if(n % 2 ==0)
        {
            new_num=n/2;

        }
        else
        {
            new_num=n*3+1;
        }
        steps.push_back(new_num);
        n=new_num;

    
    }
    for(size_t i=0;i<steps.size();i++){
        cout<<steps[i]<<endl;
    }
    return steps;

}

void dosya_yaz(vector<int> steps,int n)
{
    int c;
    ofstream file("collatz_sim.txt", ios::app);
    if(file.is_open())
    {   file<<n<<" : "<<endl;
        file<<"(";
        for (auto& c : steps)
        {
            file<<c<<",";
        }
        
        file<<")"<<endl;
        file<<"---------------------------"<<endl;
    }

    file.close();




}









int main()
{
    try
    {
        while (true)
        {
            int n;
            vector<int> dizi;
        don1:
            cout<<"collatz simulasyonu icin sayi giriniz (programdan cikmak icin \'0\' giriniz ! ) : ";
            
            if(!(cin>>n))
            {
                cout<<"hatali veri tipi girdiniz ! "<<endl;
                cin.clear();
                cin.ignore(1000,'\n');
                goto don1;
            }
            if(n<0)
            {
                cout<<"sayiyi sifir veya negatif giremezsiniz ! "<<endl;
                goto don1;
            }
            else if (n==0)
            {
                cout<<"cikiliyor..."<<endl;
                return 0;
            }
            else
            {
                dizi=collatz_sim(n);
                dosya_yaz(dizi,n);

            }
                    
                }
        
    }
    catch(const exception& e)
    {
        cerr << e.what() << '\n';
    }
    
    

    










}