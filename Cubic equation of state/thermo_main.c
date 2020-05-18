#include "thermo.h"

int main()
{
	int eqn;
	int state;
	printf("==========================================================\n");
	printf("This is calculator for Cubic Euqations of state!!\n");
	printf("-----------------------------------------------------\n");
	printf("1. vdw\n2. RK\n3. SRK\n4. PR\n");
	printf("Which eqaution do you want to calculate? : ");
	scanf("%d",&eqn);
	printf("-----------------------------------------------------\n");
	printf("1. Vapor & Vapor-like roots\n2. Liquid & Liquid-like roots\n");
	printf("Which state do you want to calculate? : ");
	scanf("%d",&state);
	printf("==========================================================\n\n");
	
	switch (eqn)
	{
	case 1:
		if(state == 1)
			vdw();
		else if(state == 2)
			vdw_l();
		else
		{
			printf("Try again please\n");
			main();
		}
		break;
	case 2:
		if(state == 1)
			rk();
		else if(state == 2)
			rk_l();
		else
		{
			printf("Try again please\n");
			main();
		}
		break;
	case 3:
		if(state == 1)
			srk();
		else if(state == 2)
			srk_l();
		else
		{
			printf("Try again please\n");
			main();
		}
		break;
	case 4:
		if(state == 1)
			pr();
		else if(state == 2)
			pr_l();
		else
		{
			printf("Try again please\n");
			main();
		}
		break;
	default:
		printf("Try again please\n");
		main();
		break;
	}
	printf("==========================================================\n");
	printf("Contact me any time if you find some error!\n");
	printf("https://github.com/exgs/hongikuniv_chemical-engineering \nsteniipion2@naver.com\n");
}