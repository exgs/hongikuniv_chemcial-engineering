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
    public partial class Form1 : Form
    {
        bool vdw_output_visable = false;
        bool rk_output_visable = false;
        bool srk_output_visable = false;
        bool pr_output_visable = false;
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void groupBox3_Enter(object sender, EventArgs e)
        {

        }

        private void groupBox2_Enter(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void vaporLike_CheckedChanged(object sender, EventArgs e)
        {
            if (this.vdw_vaporLike.Checked == true)
            {
                this.vdw_liquidLike.Checked = false;
            }
            else
            {
                this.vdw_liquidLike.Checked = true;
            }
        }

        private void liquidLike_CheckedChanged(object sender, EventArgs e)
        {
            if (this.vdw_liquidLike.Checked == true)
            {
                this.vdw_vaporLike.Checked = false;
            }
            else
            {
                this.vdw_vaporLike.Checked = true;
            }
        }

        private void groupBox5_Enter(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {

        }

        private void Tr_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void betaValue_Click(object sender, EventArgs e)
        {

        }

        private void label5_Click_1(object sender, EventArgs e)
        {
                
        }

        private void qValue_Click(object sender, EventArgs e)
        {

        }

        private void output_Enter(object sender, EventArgs e)
        {
        }

        private void VDW_Enter(object sender, EventArgs e)
        {
          
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
            int value = 0;
            try
            {
                value = int.Parse(Pr.Text) + int.Parse(Tr.Text);
            }
            catch
            {
                MessageBox.Show("Pr과 Tr에 알맞은 값을 넣어주세요.");
            }


            GroupBox output_box = (GroupBox)(this.VDW.Controls["vdw_output"]);
            Label beta = (Label)(output_box.Controls["vdw_betaValue"]);
            Label q = (Label)(output_box.Controls["vdw_qValue"]);
            Label z = (Label)(output_box.Controls["vdw_zValue"]);
            beta.Text = (value * 2).ToString(); beta.Visible = true;
            q.Text = value.ToString(); q.Visible = true;
            z.Text = (value * 4).ToString(); z.Visible = true;
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
            int value = 0;
            try
            {
                value = int.Parse(Pr.Text) + int.Parse(Tr.Text);
            }
            catch
            {
                MessageBox.Show("Pr과 Tr에 알맞은 값을 넣어주세요.");
            }

            GroupBox output_box = (GroupBox)(this.RK.Controls["rk_output"]);
            Label beta = (Label)(output_box.Controls["rk_betaValue"]);
            Label q = (Label)(output_box.Controls["rk_qValue"]);
            Label z = (Label)(output_box.Controls["rk_zValue"]);
            beta.Text = (value * 2).ToString(); beta.Visible = true;
            q.Text = value.ToString(); q.Visible = true;
            z.Text = (value * 4).ToString(); z.Visible = true;
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
            int value = 0;
            try
            {
                value = int.Parse(Pr.Text) + int.Parse(Tr.Text);
            }
            catch
            {
                MessageBox.Show("Pr과 Tr에 알맞은 값을 넣어주세요.");
            }

            GroupBox output_box = (GroupBox)(this.SRK.Controls["srk_output"]);
            Label beta = (Label)(output_box.Controls["srk_betaValue"]);
            Label q = (Label)(output_box.Controls["srk_qValue"]);
            Label z = (Label)(output_box.Controls["srk_zValue"]);
            beta.Text = (value * 2).ToString(); beta.Visible = true;
            q.Text = value.ToString(); q.Visible = true;
            z.Text = (value * 4).ToString(); z.Visible = true;
        }

        private void button1_Click(object sender, EventArgs e)
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
            int value = 0;
            try
            {
                value = int.Parse(Pr.Text) + int.Parse(Tr.Text);
            }
            catch
            {
                MessageBox.Show("Pr과 Tr에 알맞은 값을 넣어주세요.");
            }

            GroupBox output_box = (GroupBox)(this.PR.Controls["pr_output"]);
            Label beta = (Label)(output_box.Controls["pr_betaValue"]);
            Label q = (Label)(output_box.Controls["pr_qValue"]);
            Label z = (Label)(output_box.Controls["pr_zValue"]);
            beta.Text = (value * 2).ToString(); beta.Visible = true;
            q.Text = value.ToString(); q.Visible = true;
            z.Text = (value * 4).ToString(); z.Visible = true;
        }
    }
}
