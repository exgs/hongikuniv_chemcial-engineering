#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

const double ft_m = 0.3048;
const double lbm_kg = 0.4536;
const double gal_inch = 231;
const double psi_atm = 14.949;
const double atm_bar = 1.01325;
const double atm_torr = 760;

const double BTU_J = 1055;
const double cal_J = 4.184;
const double HP_W = 745;
 
const double lbf_N = 4.4482;
const double lbf_ft__J = 1.354;
const double atm_ft3__BTU = 2.7195;

const double when_0C_R = 491.67;

void print_const()
{
	printf("%lf\n",ft_m);
	printf("%lf\n",lbm_kg);
	printf("%lf\n",gal_inch);
	printf("\n");
	printf("%lf\n",psi_atm);
	printf("%lf\n",atm_bar);
	printf("%lf\n",atm_torr);
	printf("\n");
	printf("%lf\n",BTU_J);
	printf("%lf\n",cal_J);
	printf("%lf\n",HP_W);
	printf("\n");
	printf("%lf\n",when_0C_R);
	printf("\n");
	printf("%lf\n",lbf_N);
	printf("%lf\n",lbf_ft__J);
	printf("%lf\n",atm_ft3__BTU);
}

int main()
{
	int i = 0;
	int value = 0;
	char *temp_enter;
	double temp;
	srand(time(NULL));
	while (value == 0)
		value = rand()%10;
	
	printf("This is the chemical unit conversion Test\nSubmit your answer and Compare\nErrors may occur because you and i have different calculator.\nInput any integer if you don't want to solve specific question\n");
	printf("--------------------------------------------\n");
	printf("%d. %d ft = ? m\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*ft_m);
	printf("-----------------------------------\n");
	printf("%d. %d lbm = ? kg\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*lbm_kg);
	printf("-----------------------------------\n");
	printf("%d. %d gal = ? inch^3\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*gal_inch);
	printf("-----------------------------------\n");
	printf("%d. %d psi = ? atm\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*psi_atm);
	printf("-----------------------------------\n");
	printf("%d. %d atm = ? bar\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*atm_bar);
	printf("-----------------------------------\n");
	printf("%d. %d atm = ? torr\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*atm_torr);
	printf("-----------------------------------\n");
	printf("%d. %d BTU = ? J\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*BTU_J);
	printf("-----------------------------------\n");
	printf("%d. %d cal = ? J\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*cal_J);
	printf("-----------------------------------\n");
	printf("%d. %d HP = ? W\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*HP_W);
	printf("-----------------------------------\n");
	printf("%d. %d lbf = ? N\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*lbf_N);
	printf("-----------------------------------\n");
	printf("%d. %d lbf X ft = ? J\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*lbf_ft__J);
	printf("-----------------------------------\n");
	printf("%d. %d atm X ft^3 = ? BTU\n",++i, value);
	scanf("%lf",&temp);
	printf("A : %lf\n",value*atm_ft3__BTU);
	printf("-----------------------------------\n");
	
	printf("%d. temperature : 0 C = ? R\n",++i);
	scanf("%lf",&temp);
	printf("A : %lf\n",when_0C_R);
	printf("-----------------------------------\n");
	
	printf("Feedback is always welcome.\n");
	printf("Contact me dldbstjd5@naver.com OR https://github.com/exgs/hongikuniv_chemical-engineering\n");
	printf("Input [bye] to exit\n");
	scanf("%s",&temp_enter);
	printf("----------------%s------------------\n",&temp_enter);
	// print_const();
}