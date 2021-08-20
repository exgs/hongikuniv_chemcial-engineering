using System;
using System.Windows.Forms;
using EnumWindowMessage;
namespace MessageFilter
{
    class MessageFilter : System.Windows.Forms.IMessageFilter
    {

        public bool PreFilterMessage(ref System.Windows.Forms.Message m)
        {
            if (m.Msg == (int)WindowsMessage.WM_MOUSEWHEEL || m.Msg == (int)WindowsMessage.WM_SIZE)
            {
                Console.WriteLine($"{m.ToString()} : {m.Msg}");
                return true;
            }
            return false;
        }

    }
    class myInput : System.Windows.Forms.TextBox
    {
        private void Control1_GotFocus(Object sender, EventArgs e)
        {

            MessageBox.Show("You are in the Control.GotFocus event.");
        }
        public myInput()
        {
            this.SuspendLayout();
            this.Name = "myInput";
            this.AcceptsReturn = true;
            this.AcceptsTab = true;
            //this.Dock = System.Windows.Forms.DockStyle.Fill; // All the control's edges are docked to the all edges of its containing control and sized appropriately.
            this.Location = new System.Drawing.Point(15, 15);
        }
    }

    class Units
    {
        public double[] unit_list =
        {
            0.3048,
            0.4536,
            231,
            14.949,
            1.01325,
            760,

            1055,
            4.184,
            745,

            4.4482,
            1.354,
            2.7195,
            491.67
        };
    }
    class MyForm : System.Windows.Forms.Form
    {
        private TextBox textbox_temp;
        private Label answer;
        private Label unit_to;
        private int idx = 0;
        private int count = 13;
        private int value;
        Random rand = new Random();
        Units remain = new Units();
        private int[] questions = {1,2,3,4,5,6,7,8,9,10};
        private string[] unit_From = {"ft","lbm","gal","psi","atm",
                                        "atm","BTJ","cal","HP","lbf",
                                            "lbf * ft","atm * ft^3","C"};
        private string[] unit_TO = {"m","kg","inch","atm","bar",
                                        "torr","J","J","W","N",
                                            "J", "BTJ", "R"};


        // 이벤트 처리기 선언
        private void MyKeycodeHandler(object sender, System.Windows.Forms.KeyPressEventArgs e)
        {
            Console.WriteLine($"Sender : {((System.Windows.Forms.Form)sender).Text}");
            Console.WriteLine($"{e.KeyChar} : {e.Handled}");
            //Console.WriteLine($"X:{e.X}, Y:{e.Y}");
            //Console.WriteLine($"Button:{e.Button}, Clicks:{e.Clicks}");
            Console.WriteLine();
        }
        private void MySizeHandler(object sender, EventArgs e)
        {
            //this.Width = 300;
            //this.Height = 400;
            System.Windows.Forms.MessageBox.Show("Do not change Window size");
        }
        private void MyESCHandler(object sender, KeyEventArgs e)
        {
            Console.WriteLine("keydown");
            if (e.KeyCode == Keys.Escape)
            {
                //MessageBox.Show("Exit");
                Application.Exit();
            }
        }
        // UI 디자인
        private void initUIWindow()
        {
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Width = 300;
            this.Height = 150;
        }
        // 이벤트 핸들러 등록
        private void initEventHandler()
        {
            this.SizeChanged += new EventHandler(this.MySizeHandler);
            //this.MouseDown += new MouseEventHandler(this.MyMouseHandler);
            this.KeyDown += new KeyEventHandler(this.MyESCHandler);
        }


        private void initInput()
        {
            textbox_temp = new myInput();
            value = rand.Next(1, 10);
            this.Controls.Add(textbox_temp);
        
        }

        private void MyBefore(object sender, MouseEventArgs e)
        {
            value = rand.Next(1, 10);
            idx--;
            textbox_temp.Clear();
            if (idx <= 0)
            {
                idx = 0;
                answer.Text = $"{value} {unit_From[idx]}";
                unit_to.Text = unit_TO[this.idx];
                return ;
            }
            answer.Text = $"{value} {unit_From[idx]}";
            unit_to.Text = unit_TO[this.idx];
        }
        private void MyAnswer(object sender, MouseEventArgs e)
        {
            MessageBox.Show($"정답은 : {value * remain.unit_list[idx]} 입니다");
            idx++;
            if (idx >= this.count)
            {
                MessageBox.Show("수고하셨습니다.");
                Application.Exit();
            }
            value = rand.Next(1, 10);
            answer.Text = $"{value} {unit_From[idx]}";
            unit_to.Text = unit_TO[this.idx];
        }

        private void MyAfter(object sender, MouseEventArgs e)
        {
            value = rand.Next(1, 10);
            idx++;
            if (idx >= this.count)
            {
                MessageBox.Show("수고하셨습니다.");
                Application.Exit();
            }
            answer.Text = $"{value} {unit_From[idx]}";
            unit_to.Text = unit_TO[this.idx];
            //for
        }


        private void initButtonDesign()
        {
            const int interval = 60;
            const int start_x = 40;
            int Y_before_after_button = this.Height - 80;
            Button button1 = new Button();
            button1.Text = "이전";
            button1.Left = start_x;
            button1.Width -= 10;
            button1.Top = Y_before_after_button;
            button1.MouseClick += new MouseEventHandler(MyBefore);
            this.Controls.Add(button1);

            Button button2 = new Button();
            button2.Text = "다음";
            button2.Left = button1.Right + interval;
            button2.Top = Y_before_after_button;
            button2.Width -= 10;
            button2.MouseClick+= new MouseEventHandler(MyAfter);
            this.Controls.Add(button2);

            Button button3 = new Button();
            button3.Text = "정답";
            button3.Width -= 10;
            button3.Left = button1.Right;
            button3.Top = Y_before_after_button - 30;
            button3.MouseClick += new MouseEventHandler(MyAnswer);
            this.Controls.Add(button3);
        }
        private void initAnswer()
        {
            answer = new Label();
            answer.Name = "InitAnswer";
            value = rand.Next(1, 10);
            answer.Text = $"{value} {unit_From[idx]}";
            answer.Location = new System.Drawing.Point(this.Width / 2 + 15, 18);
            this.Controls.Add(answer);

            Label equal_operator = new Label();
            equal_operator.Text = " = ";
            equal_operator.Location = new System.Drawing.Point(this.Width / 2 - 5, 18);
            this.Controls.Add(equal_operator);
            unit_to = new Label();
            unit_to.Text = unit_TO[this.idx];
            unit_to.Location = new System.Drawing.Point(this.Width / 2 - 30, 18);
            this.Controls.Add(unit_to);
        }

        public MyForm()
		{
            // UI 디자인
            initUIWindow();
            // UX 디자인
            initEventHandler();
            // UI - 버튼디자인
            KeyPreview = true;
            initButtonDesign();
            
            initInput();
            initAnswer();
        }
    }

    class MainApp : Form
	{
		static void Main(string[] args)
		{

            MyForm form = new MyForm();
            Application.AddMessageFilter(new MessageFilter());
            Application.Run(form);
        }
	}
}