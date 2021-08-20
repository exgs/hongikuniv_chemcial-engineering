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
        private void resetInput()
        {

            //textBox1.Clear();
        }

        private void Control1_GotFocus(Object sender, EventArgs e)
        {

            MessageBox.Show("You are in the Control.GotFocus event.");
        }
        //public override bool AutoSize
        //{
        //    get { return base.AutoSize; }
        //    set { base.AutoSize = value; }
        //}
        public myInput()
        {
            //this.Controls.Add(Control1_GotFocus());
            this.SuspendLayout();
            this.Name = "myInput";
            this.Text = "Input value";
            //this.Clear();
            //this.ReadOnly = true;
            this.AcceptsReturn = true;
            this.AcceptsTab = true;
            //this.Dock = System.Windows.Forms.DockStyle.Fill; // All the control's edges are docked to the all edges of its containing control and sized appropriately.
            this.Location = new System.Drawing.Point(15, 15);

            //this.Width = 20;
            //this.Height = 20;
            //this.Name = "question";
            //this.Left = 50;
            //this.Top = 100;
        }
    }
    class MyForm : System.Windows.Forms.Form
    {
        private TextBox textbox_temp;
        private Label answer;
        private int idx = 0;
        private int count = 10;
        private int[] questions = {1,2,3,4,5,6,7,8,9,10};
        private string[] answers = {"a","b","ca","da","fa",
                                        "ga","ha","ja","a","a"};

    
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
            this.Controls.Add(textbox_temp);
        
        }

        private void MyBefore(object sender, MouseEventArgs e)
        {
            //Control[] temp = this.Controls.Find("myInput", false);
            //Console.WriteLine(temp.Length);
            //Console.WriteLine(temp[0]);
            idx--;
            textbox_temp.Clear();
            if (idx <= 0)
            {
                idx = 0;
                answer.Text = answers[idx];
                return ;
            }
        }

        private void MyAfter(object sender, MouseEventArgs e)
        {
            idx++;
            if (idx >= 10)
            {
                MessageBox.Show("수고하셨습니다.");
                Application.Exit();
            }
            answer.Text = answers[idx];
            //for
        }


        private void initButtonDesign()
        {
            const int interval = 50;
            const int start_x = 40;
            int Y_before_after_button = this.Height - 100;
            Button button1 = new Button();
            button1.Text = "이전 문제";
            button1.Left = start_x;
            button1.Top = Y_before_after_button;
            button1.MouseClick += new MouseEventHandler(MyBefore);
            this.Controls.Add(button1);

            Button button2 = new Button();
            button2.Text = "다음 문제";
            button2.Left = button1.Right + interval;
            button2.Top = Y_before_after_button;
            button2.MouseClick+= new MouseEventHandler(MyAfter);
            this.Controls.Add(button2);
        }
        private void initAnswer()
        {
            answer = new Label();
            answer.Name = "myAnswer";
            answer.Text = " hello world";
            answer.Location = new System.Drawing.Point(this.Width / 2, 18);
            this.Controls.Add(answer);

            Label equal_operator = new Label();
            equal_operator.Text = " = ";
            equal_operator.Location = new System.Drawing.Point(this.Width / 2 - 20, 18);
            this.Controls.Add(equal_operator);
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