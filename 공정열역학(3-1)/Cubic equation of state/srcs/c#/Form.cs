using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace cubicEquation
{
    delegate double alpha_oneArg(double Tr);
    delegate double alpha_twoArg(double Tr, double w);
    struct s_constant
    {
        public alpha_oneArg alpha_oneArg;
        public alpha_twoArg alpha_twoArg;
        public int ?alpha;
        public double sigma;
        public double upsilon;
        public double omega;
        public double psi;
        public double Zc;

        public double Pr;
        public double Tr;
        public double w;
    }
    public struct s_return
    {
        public double beta;
        public double q;
        public double z;
    }


    enum e_PhaseType
    {
        liquid,
        vapor
    }
    enum e_EquType
    {
        vdw,
        rk,
        srk,
        pr
    }

    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }


        double rk_a(double Tr)
        {
            return (1 / Math.Sqrt(Tr));
        }

        double srk_a(double Tr, double w)
        {
            return Math.Pow((1 + (0.480 + 1.574 * w - 0.176 * (Math.Pow(w, 2))) * (1 - Math.Pow(Tr, 0.5))), 2);
        }
        double pr_a(double Tr, double w)
        {
            return Math.Pow((1 + (0.37464 + 1.54226 * w - 0.26992 * (Math.Pow(w, 2))) * (1 - Math.Pow(Tr, 0.5))), 2);
        }

        private void setConstantTable(ref s_constant constants, e_EquType type, double Pr, double Tr, double w = 0)
        {
            constants.Pr = Pr;
            constants.Tr = Tr;
            constants.w = w;
            switch (type)
            {
                case e_EquType.vdw:
                    constants.alpha = 1;
                    constants.sigma = 0;
                    constants.upsilon = 0;
                    constants.omega = (double)1 / 8;
                    constants.psi = (double)27 / 64;
                    constants.Zc = (double)3 / 8;
                    break;
                case e_EquType.rk:
                    constants.alpha_oneArg = rk_a;
                    constants.sigma = 1;
                    constants.upsilon = 0;
                    constants.omega = (double)0.08664;
                    constants.psi = (double)0.42748;
                    constants.Zc = (double)1 / 3;
                    break;
                case e_EquType.srk:
                    constants.alpha_twoArg = srk_a;
                    constants.sigma = 1;
                    constants.upsilon = 0;
                    constants.omega = (double)0.08664;
                    constants.psi = (double)0.42748;
                    constants.Zc = (double)1 / 3;
                    break;
                case e_EquType.pr:
                    constants.alpha_twoArg = pr_a;
                    constants.sigma = 1 + Math.Sqrt(2);
                    constants.upsilon = 1 - Math.Sqrt(2);
                    constants.omega = (double)0.07780;
                    constants.psi = (double)0.45724;
                    constants.Zc = (double)0.30740;
                    break;
            }
        }

        private static s_return Calculating(ref s_constant constants, e_PhaseType phase, e_EquType type)
        {
            s_return value;
            value.beta = constants.omega * constants.Pr / constants.Tr;
            value.q = (constants.psi / (constants.omega * constants.Tr));
            if (type == e_EquType.vdw)
                value.q *= (double)constants.alpha;
            else if (type == e_EquType.rk)
                value.q *= (double)constants.alpha_oneArg(constants.Tr);
            else if (type == e_EquType.srk)
                value.q *= constants.alpha_twoArg(constants.Tr, constants.w);
            else
                value.q *= constants.alpha_twoArg(constants.Tr, constants.w);
            if (phase == e_PhaseType.liquid)
            {
                double Z = value.beta;
                for (int i = 0; i < 30; i++)
                {
                    Z = value.beta + (Z + constants.upsilon * value.beta) * (Z + constants.sigma * value.beta) * (1 + value.beta - Z) / (value.q * value.beta);
                }
                value.z = Z;
            }
            else
            {
                double Z = 1;
                for (int i = 0; i < 30; i++)
                {
                    Z = 1 + value.beta - (value.q * value.beta) * (Z - value.beta) / ((Z + constants.upsilon * value.beta) * (Z + constants.sigma * value.beta));
                }
                value.z = Z;
            }
            return value;
        }

        private void vdw_button_Click(object sender, EventArgs e)
        {
            GroupBox root = (GroupBox)(this.VDW.Controls["vdw_root"]);
            CheckBox vaporLike = (CheckBox)(root.Controls["vdw_vaporLike"]);
            CheckBox liquidLike = (CheckBox)(root.Controls["vdw_liquidLike"]);
            if (vaporLike.Checked == false && liquidLike.Checked == false)
            {
                MessageBox.Show("체크박스를 확인해주세요.");
                return;
            }
            
            GroupBox input_box = (GroupBox)(this.VDW.Controls["vdw_input"]);
            TextBox Pr = (TextBox)(input_box.Controls["vdw_Pr"]);
            TextBox Tr = (TextBox)(input_box.Controls["vdw_Tr"]);

            try
            {
                double test = 0;
                test = double.Parse(Pr.Text) + double.Parse(Tr.Text);
            }
            catch
            {
                MessageBox.Show("Input value에 알맞은 값을 넣어주세요.");
                return;
            }

            GroupBox output_box = (GroupBox)(this.VDW.Controls["vdw_output"]);
            Label beta = (Label)(output_box.Controls["vdw_betaValue"]);
            Label q = (Label)(output_box.Controls["vdw_qValue"]);
            Label z = (Label)(output_box.Controls["vdw_zValue"]);
            s_constant constants = new s_constant();
            s_return return_value;
            setConstantTable(ref constants, e_EquType.vdw, double.Parse(Pr.Text), double.Parse(Tr.Text));
            if (vaporLike.Checked == true)
                return_value = Calculating(ref constants, e_PhaseType.vapor, e_EquType.vdw);
            else
                return_value = Calculating(ref constants, e_PhaseType.liquid, e_EquType.vdw);

            beta.Visible = true; q.Visible = true; z.Visible = true;
            beta.Text = Math.Round(return_value.beta, 5).ToString();
            q.Text = Math.Round(return_value.q, 5).ToString();
            z.Text = Math.Round(return_value.z, 5).ToString();
        }

        private void rk_button_Click(object sender, EventArgs e)
        {
            GroupBox root = (GroupBox)(this.RK.Controls["rk_root"]);
            CheckBox vaporLike = (CheckBox)(root.Controls["rk_vaporLike"]);
            CheckBox liquidLike = (CheckBox)(root.Controls["rk_liquidLike"]);
            if (vaporLike.Checked == false && liquidLike.Checked == false)
            {
                MessageBox.Show("체크박스를 확인해주세요.");
                return;
            }

            GroupBox input_box = (GroupBox)(this.RK.Controls["rk_input"]);
            TextBox Pr = (TextBox)(input_box.Controls["rk_Pr"]);
            TextBox Tr = (TextBox)(input_box.Controls["rk_Tr"]);

            try
            {
                double test = 0;
                test = double.Parse(Pr.Text) + double.Parse(Tr.Text);
            }
            catch
            {
                MessageBox.Show("Input value에 알맞은 값을 넣어주세요.");
                return;
            }

            s_constant constants = new s_constant();
            s_return return_value;
            setConstantTable(ref constants, e_EquType.rk, double.Parse(Pr.Text), double.Parse(Tr.Text));
            if (vaporLike.Checked == true)
                return_value = Calculating(ref constants, e_PhaseType.vapor, e_EquType.rk);
            else
                return_value = Calculating(ref constants, e_PhaseType.liquid, e_EquType.rk);

            GroupBox output_box = (GroupBox)(this.RK.Controls["rk_output"]);
            Label beta = (Label)(output_box.Controls["rk_betaValue"]);
            Label q = (Label)(output_box.Controls["rk_qValue"]);
            Label z = (Label)(output_box.Controls["rk_zValue"]);
            beta.Visible = true; q.Visible = true; z.Visible = true;
            beta.Text = Math.Round(return_value.beta, 5).ToString();
            q.Text = Math.Round(return_value.q, 5).ToString();
            z.Text = Math.Round(return_value.z, 5).ToString();
        }

        private void sdk_button_Click(object sender, EventArgs e)
        {
            GroupBox root = (GroupBox)(this.SRK.Controls["srk_root"]);
            CheckBox vaporLike = (CheckBox)(root.Controls["srk_vaporLike"]);
            CheckBox liquidLike = (CheckBox)(root.Controls["srk_liquidLike"]);
            if (vaporLike.Checked == false && liquidLike.Checked == false)
            {
                MessageBox.Show("체크박스를 확인해주세요.");
                return;
            }

            GroupBox input_box = (GroupBox)(this.SRK.Controls["srk_input"]);
            TextBox Pr = (TextBox)(input_box.Controls["srk_Pr"]);
            TextBox Tr = (TextBox)(input_box.Controls["srk_Tr"]);
            TextBox w = (TextBox)(input_box.Controls["srk_w"]);
 
            try
            {
                double test = 0;
                test = double.Parse(Pr.Text) + double.Parse(Tr.Text) + double.Parse(w.Text);
            }
            catch
            {
                MessageBox.Show("Input value에 알맞은 값을 넣어주세요.");
                return;
            }

            s_constant constants = new s_constant();
            s_return return_value;
            setConstantTable(ref constants, e_EquType.srk, double.Parse(Pr.Text), double.Parse(Tr.Text), double.Parse(w.Text));
            if (vaporLike.Checked == true)
                return_value = Calculating(ref constants, e_PhaseType.vapor, e_EquType.srk);
            else
                return_value = Calculating(ref constants, e_PhaseType.liquid, e_EquType.srk);

            GroupBox output_box = (GroupBox)(this.SRK.Controls["srk_output"]);
            Label beta = (Label)(output_box.Controls["srk_betaValue"]);
            Label q = (Label)(output_box.Controls["srk_qValue"]);
            Label z = (Label)(output_box.Controls["srk_zValue"]);
            beta.Visible = true; q.Visible = true; z.Visible = true;
            beta.Text = Math.Round(return_value.beta, 5).ToString();
            q.Text = Math.Round(return_value.q, 5).ToString();
            z.Text = Math.Round(return_value.z, 5).ToString();
        }

        private void pr_button_Click(object sender, EventArgs e)
        {
            GroupBox root = (GroupBox)(this.PR.Controls["pr_root"]);
            CheckBox vaporLike = (CheckBox)(root.Controls["pr_vaporLike"]);
            CheckBox liquidLike = (CheckBox)(root.Controls["pr_liquidLike"]);
            if (vaporLike.Checked == false && liquidLike.Checked == false)
            {
                MessageBox.Show("체크박스를 확인해주세요.");
                return;
            }

            GroupBox input_box = (GroupBox)(this.PR.Controls["pr_input"]);
            TextBox Pr = (TextBox)(input_box.Controls["pr_Pr"]);
            TextBox Tr = (TextBox)(input_box.Controls["pr_Tr"]);
            TextBox w = (TextBox)(input_box.Controls["pr_w"]);
            try
            {
                double test = 0;
                test = double.Parse(Pr.Text) + double.Parse(Tr.Text) + double.Parse(w.Text);
            }
            catch
            {
                MessageBox.Show("Input value에 알맞은 값을 넣어주세요.");
                return;
            }

            s_constant constants = new s_constant();
            s_return return_value;
            setConstantTable(ref constants, e_EquType.pr, double.Parse(Pr.Text), double.Parse(Tr.Text), double.Parse(w.Text));
            if (vaporLike.Checked == true)
                return_value = Calculating(ref constants, e_PhaseType.vapor, e_EquType.pr);
            else
                return_value = Calculating(ref constants, e_PhaseType.liquid, e_EquType.pr);

            GroupBox output_box = (GroupBox)(this.PR.Controls["pr_output"]);
            Label beta = (Label)(output_box.Controls["pr_betaValue"]);
            Label q = (Label)(output_box.Controls["pr_qValue"]);
            Label z = (Label)(output_box.Controls["pr_zValue"]);
            beta.Visible = true; q.Visible = true; z.Visible = true;
            beta.Text = Math.Round(return_value.beta, 5).ToString();
            q.Text = Math.Round(return_value.q, 5).ToString();
            z.Text = Math.Round(return_value.z, 5).ToString();
        }

        private void vaporLike_CheckedChanged(object sender, EventArgs e)
        {
            if (this.vdw_vaporLike.Checked == true)
                this.vdw_liquidLike.Checked = false;
        }

        private void liquidLike_CheckedChanged(object sender, EventArgs e)
        {
            if (this.vdw_liquidLike.Checked == true)
                this.vdw_vaporLike.Checked = false;
        }
        private void rk_vaporLike_CheckedChanged(object sender, EventArgs e)
        {
            if (this.rk_vaporLike.Checked == true)
                this.rk_liquidLike.Checked = false;
        }

        private void rk_liquidLike_CheckedChanged(object sender, EventArgs e)
        {
            if (this.rk_liquidLike.Checked == true)
                this.rk_vaporLike.Checked = false;
        }

        private void srk_vaporLike_CheckedChanged(object sender, EventArgs e)
        {
            if (this.srk_vaporLike.Checked == true)
                this.srk_liquidLike.Checked = false;
        }

        private void srk_liquidLike_CheckedChanged(object sender, EventArgs e)
        {
            if (this.srk_liquidLike.Checked == true)
                this.srk_vaporLike.Checked = false;
        }

        private void pr_vaporLike_CheckedChanged(object sender, EventArgs e)
        {
            if (this.pr_vaporLike.Checked == true)
                this.pr_liquidLike.Checked = false;
        }

        private void pr_liquidLike_CheckedChanged(object sender, EventArgs e)
        {
            if (this.pr_liquidLike.Checked == true)
                this.pr_vaporLike.Checked = false;
        }
    }
}
