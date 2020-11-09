#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int strEqual(char *s1,char*s2)
{
	int i;
	for(i=0;s1[i]!='\0'&&s2[i]!='\0';i++)
		if(s1[i] != s2[i])
			return 0;
	return 1;
}
int main()
{
	int n,i,j,k,flag;
	scanf("%d",&n);
	while(n--){
		char w[3][3][13];
		int coin[12] = {1,1,1,1,1,1,1,1,1,1,1,1};
		for(i=0;i<3;i++)
			scanf("%s%s%s",w[i][0],w[i][1],w[i][2]);
		for(i=0;i<12;i++)
			for(j=-1;j<2;j+=2)
			{
				flag = 1;
				for(k=0;k<3;k++)
				{
					int coin[12] = {1,1,1,1,1,1,1,1,1,1,1,1};
					coin[i] += j;
					int w1=0,w2=0,m;
					for(m=0;m<strlen(w[k][0]);m++){
						w1 += coin[w[k][0][m]-'A'];
						w2 += coin[w[k][1][m]-'A'];
					}
					if(strEqual(w[k][2],"even") && !(w1 == w2))
						flag = 0;
					else if(strEqual(w[k][2],"up") && !(w1 > w2))
						flag = 0;
					else if(strEqual(w[k][2],"down") && !(w1 < w2))
						flag = 0;
				}
				if(flag == 1){
					if(j == -1)
						printf("%c is the counterfeit coin and it is light.\n",'A' + i);
					else
						printf("%c is the counterfeit coin and it is heavy.\n",'A' + i);
				}
			}
		
	}
	return 0;
} 