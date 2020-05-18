#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct s_table
{
	void * a_eqn;
	int a;
	double sigma;
	double upsilon;
	double omega;
	double psi;
	double Zc;
}				t_table;


void vdw();
void rk();
double rk_a (double Tr);
void srk();
double srk_a(double Tr, double w);
void pr();
double pr_a(double Tr, double w);
void vdw_l();
void rk_l();
void srk_l();
void pr_l();