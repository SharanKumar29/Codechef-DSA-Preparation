#include <stdio.h>

int main(void) {
	int t;
	scanf("%d",&t);
	while(t--)
	{
	    long int n,sum=0,cou=0;
	    scanf("%ld",&n);
	    
	    char s[n+1];
	    scanf("%s",&s);
	    
	    for (int i=0;i<n;i++)
	    {
	       if (s[i]=='0'){
	           cou+=1; 
	       }
	       else{
	            sum+=cou;
	       }
	    }
        sum=(sum%(1000000000+7));
	    printf("%ld\n",sum);	
	    
	}
	return 0;
}
