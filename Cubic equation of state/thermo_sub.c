#include "thermo.h"

void vdw()
{
	printf("This is equation of VDW(Van der waals) [Vapor-Vapor]\n");
	printf("Please enter Decimal value, Not Symbolic value (S<=>D)\n");
	double Tr;
	double Pr;
	printf("Tr = ");
	scanf("%lf",&Tr);
	printf("Pr = ");
	scanf("%lf",&Pr);	
	double Z = 1;
	double beta;
	double q;
	int a = 1;
	t_table value;
	value.sigma = 0;
	value.upsilon = 0;
	value.omega = 0.125;
	value.psi = 27/(double)64;
	value.Zc = 3/(double)8;
	value.a_eqn = (int *)&a;
	beta =value.omega*(Pr/Tr);
	q = value.psi/value.omega * (*(int *)value.a_eqn)/Tr;
	printf("beta : %lf\n",beta);
	printf("q : %lf\n",q);
	printf("------------------------------\n\n");
	for (size_t i = 0; i < 10; i++)
	{
		Z = 1 + beta - (q*beta)*(Z-beta)/((Z + value.upsilon * beta) * (Z + value.sigma * beta));
	}
	
	printf("Z: %lf\n",Z);
	return;
}

void vdw_l()
{
	printf("This is equation of VDW(Van der waals) [liquid-liquid]\n");
	printf("Please enter Decimal value, Not Symbolic value (S<=>D)\n");
	double Tr;
	double Pr;
	printf("Tr = ");
	scanf("%lf",&Tr);
	printf("Pr = ");
	scanf("%lf",&Pr);	
	double Z = 1;
	double beta;
	double q;
	int a = 1;
	t_table value;
	value.sigma = 0;
	value.upsilon = 0;
	value.omega = 0.125;
	value.psi = 27/(double)64;
	value.Zc = 3/(double)8;
	value.a_eqn = (int *)&a;
	beta =value.omega*(Pr/Tr);
	q = value.psi/value.omega * (*(int *)value.a_eqn)/Tr;
	printf("beta : %lf\n",beta);
	printf("q : %lf\n",q);
	printf("------------------------------\n\n");
	Z = beta; // 최초로 넣어주는 값
	for (size_t i = 0; i < 10; i++)
	{
		Z = beta + (Z + value.upsilon * beta) * (Z + value.sigma * beta) * (1 + beta - Z) / (q * beta);
	}
	
	printf("Z: %lf\n",Z);
	return;
}

double rk_a (double Tr)
{
	return (1/sqrt(Tr));
}

void rk()
{
	printf("This is equation of RK(Redlich/Kwong) [Vapor-Vapor]\n");
	printf("Please enter Decimal value, Not Symbolic value (S<=>D)\n");
	double Tr;
	double Pr;
	printf("Tr = ");
	scanf("%lf",&Tr);
	printf("Pr = ");
	scanf("%lf",&Pr);	
	double Z = 1; // 최초에 넣어주는 값
	double beta;
	double q;
	t_table value;
	value.sigma = 1;
	value.upsilon = 0;
	value.omega = 0.08664;
	value.psi = 0.42748;
	value.Zc = 1/(double)3;
	double (*f) (double) = rk_a; // 함수포인터 선언
	value.a_eqn = f; // 함수 포인터를 변수에 담기 (void *)
	beta =value.omega*(Pr/Tr);
	q = value.psi/value.omega * (((double (*)(double))value.a_eqn)(Tr))/Tr;
	printf("q : %lf\n",q);
	printf("beta : %lf\n",beta);
	// printf("---------\n");
	printf("------------------------------\n\n");
	for (size_t i = 0; i < 30; i++)
	{
		Z = 1 + beta - (q*beta)*(Z-beta)/((Z + value.upsilon * beta) * (Z + value.sigma * beta));
	}
	printf("Z: %lf\n",Z);
	return;
}

void rk_l()
{
	printf("This is equation of RK(Redlich/Kwong) [Liquid-Liquid]\n");
	printf("Please enter Decimal value, Not Symbolic value (S<=>D)\n");
	double Tr;
	double Pr;
	printf("Tr = ");
	scanf("%lf",&Tr);
	printf("Pr = ");
	scanf("%lf",&Pr);	
	double Z = 1; // 최초에 넣어주는 값
	double beta;
	double q;
	t_table value;
	value.sigma = 1;
	value.upsilon = 0;
	value.omega = 0.08664;
	value.psi = 0.42748;
	value.Zc = 1/(double)3;
	double (*f) (double) = rk_a; // 함수포인터 선언
	value.a_eqn = f; // 함수 포인터를 변수에 담기 (void *)
	beta =value.omega*(Pr/Tr);
	q = value.psi/value.omega * (((double (*)(double))value.a_eqn)(Tr))/Tr;
	printf("q : %lf\n",q);
	printf("beta : %lf\n",beta);
	// printf("---------\n");
	printf("------------------------------\n\n");
	Z = beta; // 최초로 넣어주는 값
	for (size_t i = 0; i < 30; i++)
	{
		Z = beta + (Z + value.upsilon * beta) * (Z + value.sigma * beta) * (1 + beta - Z) / (q * beta);
	}
	printf("Z: %lf\n",Z);
	return;
}

double srk_a(double Tr, double w)
{
	return pow((1 + (0.480 + 1.574*w - 0.176*(pow(w,2))) * (1 - pow(Tr,0.5))), 2);
}

void srk()
{
	printf("This is equation of SRK(Soave/Redlich/Kwong) [Vapor-Vapor]\n");
	printf("Please enter Decimal value, Not Symbolic value (S<=>D)\n");
	double Tr;
	double Pr;
	double w;
	printf("Tr = ");
	scanf("%lf",&Tr);
	printf("Pr = ");
	scanf("%lf",&Pr);
	printf("w = ");
	scanf("%lf",&w);
	double Z = 1;
	double beta;
	double q;
	t_table value;
	value.sigma = 1;
	value.upsilon = 0;
	value.omega = 0.08664;
	value.psi = 0.42748;
	value.Zc = 1/(double)3;
	double (*f) (double, double) = srk_a; // 함수포인터 선언
	value.a_eqn = f; // 함수 포인터를 변수에 담기 (void *)
	beta =value.omega*(Pr/Tr);
	q = value.psi/value.omega * (((double (*)(double, double))value.a_eqn)(Tr, w))/Tr;
	printf("q : %lf\n",q);
	printf("q : %lf\n",q);
	printf("beta : %lf\n",beta);
	// printf("---------\n");
	printf("------------------------------\n\n");
	for (size_t i = 0; i < 30; i++)
	{
		Z = 1 + beta - (q*beta)*(Z-beta)/((Z + value.upsilon * beta) * (Z + value.sigma * beta));
	}
	printf("Z: %lf\n",Z);
	return;
}

void srk_l()
{
	printf("This is equation of SRK(Soave/Redlich/Kwong) [Liquid-Liquid]\n");
	printf("Please enter Decimal value, Not Symbolic value (S<=>D)\n");
	double Tr;
	double Pr;
	double w;
	printf("Tr = ");
	scanf("%lf",&Tr);
	printf("Pr = ");
	scanf("%lf",&Pr);
	printf("w = ");
	scanf("%lf",&w);
	double Z = 1;
	double beta;
	double q;
	t_table value;
	value.sigma = 1;
	value.upsilon = 0;
	value.omega = 0.08664;
	value.psi = 0.42748;
	value.Zc = 1/(double)3;
	double (*f) (double, double) = srk_a; // 함수포인터 선언
	value.a_eqn = f; // 함수 포인터를 변수에 담기 (void *)
	beta =value.omega*(Pr/Tr);
	q = value.psi/value.omega * (((double (*)(double, double))value.a_eqn)(Tr, w))/Tr;
	printf("q : %lf\n",q);
	printf("beta : %lf\n",beta);
	// printf("---------\n");
	printf("------------------------------\n\n");
	Z = beta; // 최초로 넣어주는 값
	for (size_t i = 0; i < 30; i++)
	{
		Z = beta + (Z + value.upsilon * beta) * (Z + value.sigma * beta) * (1 + beta - Z) / (q * beta);
	}
	printf("Z: %lf\n",Z);
	return;
}

double pr_a(double Tr, double w)
{
	return pow((1 + (0.37464 + 1.54226*w - 0.26992*(pow(w,2))) * (1 - pow(Tr,0.5))), 2);
}

void pr()
{
	printf("This is equation of PR(Peng/Robinson) [Vapor-Vapor]\n");
	printf("Please enter Decimal value, Not Symbolic value (S<=>D)\n");
	double Tr;
	double Pr;
	double w;
	printf("Tr = ");
	scanf("%lf",&Tr);
	printf("Pr = ");
	scanf("%lf",&Pr);
	printf("w = ");
	scanf("%lf",&w);
	double Z = 1;
	double beta;
	double q;
	t_table value;
	value.sigma = 1 + pow(2,0.5);
	value.upsilon = 1 - pow(2,0.5);
	value.omega = 0.07780;
	value.psi = 0.45724;
	value.Zc = 0.30740;
	double (*f) (double, double) = pr_a; // 함수포인터 선언
	value.a_eqn = f; // 함수 포인터를 변수에 담기 (void *)
	beta =value.omega*(Pr/Tr);
	q = value.psi/value.omega * (((double (*)(double, double))value.a_eqn)(Tr, w))/Tr;
	printf("q : %lf\n",q);
	printf("beta : %lf\n",beta);
	// printf("---------\n");
	printf("------------------------------\n\n");
	for (size_t i = 0; i < 30; i++)
	{
		Z = 1 + beta - (q*beta)*(Z-beta)/((Z + value.upsilon * beta) * (Z + value.sigma * beta));
	}
	printf("Z: %lf\n",Z);
	return;
}

void pr_l()
{
	printf("This is equation of PR(Peng/Robinson) [Liquid-Liquid]\n");
	printf("Please enter Decimal value, Not Symbolic value (S<=>D)\n");
	double Tr;
	double Pr;
	double w;
	printf("Tr = ");
	scanf("%lf",&Tr);
	printf("Pr = ");
	scanf("%lf",&Pr);
	printf("w = ");
	scanf("%lf",&w);
	double Z = 1;
	double beta;
	double q;
	t_table value;
	value.sigma = 1 + pow(2,0.5);
	value.upsilon = 1 - pow(2,0.5);
	value.omega = 0.07780;
	value.psi = 0.45724;
	value.Zc = 0.30740;
	double (*f) (double, double) = pr_a; // 함수포인터 선언
	value.a_eqn = f; // 함수 포인터를 변수에 담기 (void *)
	beta =value.omega*(Pr/Tr);
	q = value.psi/value.omega * (((double (*)(double, double))value.a_eqn)(Tr, w))/Tr;
	printf("q : %lf\n",q);
	printf("beta : %lf\n",beta);
	// printf("---------\n");
	printf("------------------------------\n\n");
	Z = beta; // 최초로 넣어주는 값
	for (size_t i = 0; i < 30; i++)
	{
		Z = beta + (Z + value.upsilon * beta) * (Z + value.sigma * beta) * (1 + beta - Z) / (q * beta);
	}
	printf("Z: %lf\n",Z);
	return;
}