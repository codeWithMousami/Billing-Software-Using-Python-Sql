from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk   #pip3 install Pillow
from PIL import Image
import random, os
from tkinter import messagebox
import tempfile
from time import strftime


class Bill_App:
    def __init__(self,root):
        self.root= root
        self.root.geometry('1530x800+0+0')
        self.root.title('Billing Software')


        # ======================Variables===============================

        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()

        z=random.randint(1000,9999)
        self.bill_no.set(z)

        self.c_email= StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()

        #========================Product Category List ========================

        self.Category=['Select option','Clothing','Lifestyle','Mobiles']

        #sub-category clothing 

        self.SubCatClothing=['Pant','T-Shirt','Shirt']
        self.pant=['Levis','Mufti','Spykar']
        self.price_levis=5000
        self.price_mufti=700
        self.price_spykar=8000


        self.T_Shirt=['Polo','Roadster','Jack&Jones']
        self.price_Polo=1500
        self.price_Roadstar=1800
        self.price_JackJones=1700

        self.Shirt=['Peter England ','Louis Phillipe','Park Avenue']
        self.price_Peter=2100
        self.price_Louis=2700
        self.price_Park=1740

        #Sub-Cat Lifestyle

        self.SubCatLifestyle=['Bath Soap','Face Cream','Hair Oil']
        self.Bath_soap=['Lifebuy','Lux','Santoor','Pearl']
        self.price_life=20
        self.price_lux=20
        self.price_santoor=20
        self.price_pearl=30


        self.Face_cream=['Glow&Lovely','Ponds','Olay','Garnier']
        self.price_glow=20
        self.price_ponds=20
        self.price_olay=20
        self.price_garnier=30


        self.Hair_oil=['Parachute','Jashmin','Bajaj']
        self.price_para=25
        self.price_jashmin=22
        self.price_bajaj=30


        
        #sub-category mobile


        self.SubCatMobiles=['Iphone','Samsung','Xiome','Real Me','Others']

        self.Iphone=['Iphone_X','Iphone_11','Iphone_12']
        self.price_ix=40000
        self.price_i11=60000
        self.price_i12=85000

        self.Samsung=['Samsumg M16','Samsumg M12','Samsung M21']
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000
       

        self.Xiome=['Red 11','Readme-12','ReadmePro']
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000

        self.RealMe=['RealMe  12','RealMe  13','Realme Pro']
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=30000

        self.OnePlus=['OnePlus 1','OnePlus 2','OnePlus 3']
        self.price_one1=45000
        self.price_one2=60000
        self.price_one3=45800











        self.SubCatLifeStyle=['Bath Soap','Face Cream','Hair Oil']
        self.SubCatMobiles=['Iphone','Sumsung','Xiomi','RealMe','One Plus']

#image 1
        img= Image.open('image/b1.jpg')
        img = img.resize((500, 130), Image.BICUBIC)
        self.photoimg= ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0, y=0, width=500, height=130)

#image 2
        img1= Image.open('image/girls.jpg')
        img1 = img1.resize((500, 130), Image.BICUBIC)
        self.photoimg1= ImageTk.PhotoImage(img1)
        lbl_img1=Label(self.root,image=self.photoimg1)
        lbl_img1.place(x=500, y=0, width=500, height=130)

#image 3
        img2= Image.open('image/girl1.jpg')
        img2 = img2.resize((540, 130), Image.BICUBIC)
        self.photoimg2= ImageTk.PhotoImage(img2)
        lbl_img2=Label(self.root,image=self.photoimg2)
        lbl_img2.place(x=1000, y=0, width=540, height=130)

#label title
        lbl_title=Label(self.root,text='BILLING SOFTWARE ',font=('times new roman ', 35,'bold'),bg='white',fg='red')
        lbl_title.place(x=0, y=130, width=1530, height=45)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(lbl_title,font=('times new roman ', 16,'bold'),background='white',foreground='blue') 
        lbl.place(x=0,y=0,width=120,height=45)   
        time()

#main frame down the title
        Main_Frame = Frame(self.root,bd=5,relief=GROOVE,bg='white')
        Main_Frame.place(x=0, y=175, width=1530, height=620)

#sub frame Customer
        Cust_Frame =LabelFrame(Main_Frame,text='Customer',font=('times new roman ', 12,'bold'),bg='white',fg='red')
        Cust_Frame.place(x=10, y=5, width=350, height=140)

        self.lbl_mob=Label(Cust_Frame,text='Mobile No.',font=('times new roman ', 12,'bold'),bg='white')
        self.lbl_mob.grid(row=0, column=0, stick=W, padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phon,font=('times new roman ', 10,'bold'),width=24)
        self.entry_mob.grid(row=0,column=1)               

        self.lblCustname=Label(Cust_Frame,font=('arial ', 12,'bold'),bg='white',text='Customer Name',bd=4)
        self.lblCustname.grid(row=1, column=0, stick=W, padx=5,pady=2)

        self.txtCustname=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('arial ', 10,'bold'),width=24)
        self.txtCustname.grid(row=1,column=1, stick=W, padx=5,pady=2)               

        self.lblEmail=Label(Cust_Frame,text='Email',font=('arial ', 12,'bold'),bg='white',bd=4)
        self.lblEmail.grid(row=2, column=0, stick=W, padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('arial', 10,'bold'),width=24)
        self.txtEmail.grid(row=2,column=1, stick=W, padx=5,pady=2)      


#sub frame Product
        Product_Frame =LabelFrame(Main_Frame,text='Product',font=('times new roman ', 12,'bold'),bg='white',fg='red')
        Product_Frame.place(x=370, y=5, width=610, height=140) 

          #category
        
        self.lblCategory=Label(Product_Frame,text='Select Category',font=('times new roman ', 12,'bold'),bg='white')
        self.lblCategory.grid(row=0, column=0, stick=W, padx=5,pady=2)   

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',10,'bold'),width=24,state='readonly')      
        self.Combo_Category.current(0)       
        self.Combo_Category.grid(row=0,column=1,stick=W, padx=5,pady=2)    
        self.Combo_Category.bind('<<ComboboxSelected>>',self.Categories)


#sub category

        self.lblSubCategory=Label(Product_Frame,text='Subcategory',font=('times new roman ', 12,'bold'),bg='white')
        self.lblSubCategory.grid(row=1, column=0, stick=W, padx=5,pady=2)   

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[''],font=('arial',10,'bold'),width=24,state='readonly')             
        self.ComboSubCategory.grid(row=1,column=1,stick=W, padx=5,pady=2)
        self.ComboSubCategory.bind('<<ComboboxSelected>>',self.Product_add)


        
#Product Name

        self.lblProduct=Label(Product_Frame,text='Product Name',font=('times new roman ', 12,'bold'),bg='white')
        self.lblProduct.grid(row=2, column=0, stick=W, padx=5,pady=2)   

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=('arial',10,'bold'),width=24,state='readonly')             
        self.ComboProduct.grid(row=2,column=1,stick=W, padx=5,pady=2)
        self.ComboProduct.bind('<<ComboboxSelected>>',self.price)


#Price

        self.lblPrice=Label(Product_Frame,text='Price',font=('times new roman ', 12,'bold'),bg='white')
        self.lblPrice.grid(row=0, column=2, stick=W, padx=5,pady=2)   

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=('arial',10,'bold'),width=24,state='readonly')             
        self.ComboPrice.grid(row=0,column=3,stick=W, padx=5,pady=2)


#Quantity

        self.lblQty=Label(Product_Frame,text='Qty',font=('times new roman ', 12,'bold'),bg='white')
        self.lblQty.grid(row=1, column=2, stick=W, padx=5,pady=2)   

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',11,'bold'),width=24)             
        self.ComboQty.grid(row=1,column=3,stick=W, padx=5,pady=2)

 #Middle Frame

        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)   

#image 1
        
        img12= Image.open('image/good.jpg')
        img12 = img12.resize((490, 340), Image.BICUBIC)
        self.photoimg12= ImageTk.PhotoImage(img12)

        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=0, y=0, width=490, height=340)

#image 2
        img13= Image.open('image/mall.jpg')
        img13 = img13.resize((490, 340), Image.BICUBIC)
        self.photoimg13= ImageTk.PhotoImage(img13)

        lbl_img13=Label(MiddleFrame,image=self.photoimg13)
        lbl_img13.place(x=490, y=0, width=500, height=340)    

  #Search
        Search_Frame= Frame(Main_Frame,bd=2,bg='white')
        Search_Frame.place(x=1020,y=15,width=500,height=40)

        self.lblBill=Label(Search_Frame,text='Bill Number',font=('times new roman ', 12,'bold'),bg='red',fg='White')
        self.lblBill.grid(row=0, column=0, stick=W, padx=1)  

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',11,'bold'),width=24)             
        self.txt_Entry_Search.grid(row=0,column=1,stick=W, padx=2)

        self.BtnSearch= Button(Search_Frame,command=self.find_bill,text='Search',font=('arial',10,'bold'),bg='orangered',width=15,fg='white',cursor='hand2')
        self.BtnSearch.grid(row=0,column=2)

#Right Frame Bill Area

        RightLabelFrame= LabelFrame(Main_Frame,text='Bill Area',font=('times new roman ', 12,'bold'),bg='white',fg='red')
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)       

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL) 
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg='white',fg='blue',font=('times new roman ', 12,'bold'))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

#Bill Counter Label Frame
        Bottom_Frame =LabelFrame(Main_Frame,text='Bill Counter',font=('times new roman ', 12,'bold'),bg='white',fg='red')
        Bottom_Frame.place(x=0, y=485, width=1520, height=125) 


        
        self.lblSubTotal=Label(Bottom_Frame,text='Sub Total',font=('times new roman ', 12,'bold'),bg='white',bd=4)
        self.lblSubTotal.grid(row=0, column=0, stick=W, padx=5,pady=2)   

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=('arial',11,'bold'),width=24)             
        self.EntrySubTotal.grid(row=0,column=1,stick=W, padx=5,pady=2)

        self.lbl_Tax=Label(Bottom_Frame,text='Gov Tax',font=('times new roman ', 12,'bold'),bg='white',bd=4)
        self.lbl_Tax.grid(row=1, column=0, stick=W, padx=5,pady=2)   

        self.txt_Tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=('arial',11,'bold'),width=24)             
        self.txt_Tax.grid(row=1,column=1,stick=W, padx=5,pady=2)


        self.lblAmountTotal=Label(Bottom_Frame,text='Total',font=('times new roman ', 12,'bold'),bg='white',bd=4)
        self.lblAmountTotal.grid(row=2, column=0, stick=W, padx=5,pady=2)   

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=('arial',11,'bold'),width=24)             
        self.txtAmountTotal.grid(row=2,column=1,stick=W, padx=5,pady=2)


#Button Frame
        Btn_Frame= Frame(Bottom_Frame,bd=2,bg='white')
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart= Button(Btn_Frame,command=self.AddItem,text='Add To Cart',height=2,font=('arial',15,'bold'),bg='orangered',fg='white',width=15,cursor='hand2')
        self.BtnAddToCart.grid(row=0,column=0)

        self.BtnGenearte_bill= Button(Btn_Frame,command=self.gen_bill,text='Generate Bill',height=2,font=('arial',15,'bold'),bg='orangered',width=15,fg='white',cursor='hand2')
        self.BtnGenearte_bill.grid(row=0,column=1)

        self.BtnSave= Button(Btn_Frame,text='Save Bill',command=self.save_bill,height=2,font=('arial',15,'bold'),bg='orangered',width=15,fg='white',cursor='hand2')
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint= Button(Btn_Frame,command=self.iprint,text='Print',height=2,font=('arial',15,'bold'),bg='orangered',width=15,fg='white',cursor='hand2')
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear= Button(Btn_Frame,command=self.clear,text='Clear',height=2,font=('arial',15,'bold'),bg='orangered',width=15,fg='white',cursor='hand2')
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit= Button(Btn_Frame,command=self.root.destroy,text='Exit',height=2,font=('arial',15,'bold'),bg='orangered',width=15,fg='white',cursor='hand2')
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]

    

        #=================================FUNCTION DECLARTION ================================
    def AddItem(self):  
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=='':
            messagebox.showerror('Error','Please Select The Product Name')
        else:
            self.textarea.insert(END,f'\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}')   
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l)))) 
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l))+((((sum(self.l))-(self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=='':
            messagebox.showerror('Error','Please Add To Cart Product')
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l)))) 
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,' \n==================================================')
            self.textarea.insert(END,f'\n Sub Amount :\t\t\t {self.sub_total.get()}')
            self.textarea.insert(END,f'\n Tax Amount :\t\t\t {self.tax_input.get()}')
            self.textarea.insert(END,f'\n Total Amount :\t\t\t {self.total.get()}')
            self.textarea.insert(END,'\n==================================================')



    def save_bill(self):
        op=messagebox.askyesno('Save Bill','Do You want To save The Bill')
        if op>0 :
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+'.txt','w')
            f1.write(self.bill_data)
            op=messagebox.showinfo('Saved',f'Bill No : {self.bill_no.get()}saved successfully')
            f1.close()
            
    def iprint(self):
        q=self.textarea.get(1.0,'end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,'print')
    
    def find_bill(self):
        found='no'
        for i in  os.listdir('bills/'):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found='yes'
            
        if found=='no':
            messagebox.showerror('Error','Invalid Bill No.')  


    
             

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set('')
        self.c_phon.set('')
        self.c_email.set('')
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set('')
        self.product.set('')
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.sub_total.set('')
        self.tax_input.set('')
        self.total.set('')
        self.welcome()


    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,'\t Welcome To The Mini Mall')
        self.textarea.insert(END,f'\n Bill Number : {self.bill_no.get()}')    
        self.textarea.insert(END,f'\n Customer Name : {self.c_name.get()}') 
        self.textarea.insert(END,f'\n Phone Number: {self.c_phon.get()}') 
        self.textarea.insert(END,f'\n Customer Email : {self.c_email.get()}') 

        self.textarea.insert(END,'\n==================================================')
        self.textarea.insert(END,f'\n Products\t\t\tQTY\t\tPrice') 
        self.textarea.insert(END,'\n==================================================\n')
    
    def Categories(self, event=''):
        if self.Combo_Category.get()=='Clothing':
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=='Lifestyle':
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)

        if self.Combo_Category.get()=='Mobiles':
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)    

    def Product_add(self,event=''):
        if self.ComboSubCategory.get()=='Pant':
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=='T-Shirt':
            self.ComboProduct.config(value=self.T_Shirt)
            self.ComboProduct.current(0)

        if self.ComboSubCategory.get()=='Shirt':
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)   


        #Lifestyle
           #'Bath Soap','Face Cream','Hair Oil' 
        if self.ComboSubCategory.get()=='Bath Soap':
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0) 

        if self.ComboSubCategory.get()=='Face Cream':
            self.ComboProduct.config(value=self.Face_cream)
            self.ComboProduct.current(0) 

        if self.ComboSubCategory.get()=='Hair Oil':
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)   


        #Mobiles
        #Iphone','Sumsung','Xiomi','RealMe','One Plus
            
        if self.ComboSubCategory.get()=='Iphone':
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0) 

        if self.ComboSubCategory.get()=='Sumsung':
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0) 

        if self.ComboSubCategory.get()=='Xiomi':
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0) 

        if self.ComboSubCategory.get()=='RealMe':
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0) 

        if self.ComboSubCategory.get()=='One Plus':
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0) 

    def price(self,event=''):
        #pant
        #'Levis','Mufti','Spykar'
        if self.ComboProduct.get()=='Levis':
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)    
            self.qty.set(1)  

        if self.ComboProduct.get()=='Mufti':
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        if self.ComboProduct.get()=='Spykar':
            self.ComboPrice.config(value=self.price_spykar)
            self.ComboPrice.current(0)    
            self.qty.set(1) 

        #T-shirt
        #Polo','Roadster','Jack&Jones    
        if self.ComboProduct.get()=='Polo':
            self.ComboPrice.config(value=self.price_Polo)
            self.ComboPrice.current(0)    
            self.qty.set(1)  

        if self.ComboProduct.get()=='Roadster':
            self.ComboPrice.config(value=self.price_Roadstar)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        if self.ComboProduct.get()=='Jack&Jones':
            self.ComboPrice.config(value=self.price_JackJones)
            self.ComboPrice.current(0)    
            self.qty.set(1)  

        #Shirt
        #Peter England ','Louis Phillipe','Park Avenue
            
        if self.ComboProduct.get()=='Peter England':
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)    
            self.qty.set(1)  

        if self.ComboProduct.get()=='Louis Phillipe':
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        if self.ComboProduct.get()=='Park Avenue':
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0)    
            self.qty.set(1) 

        #bath soap
        #Lifebuy','Lux','Santoor','Pearl    
            
        if self.ComboProduct.get()=='Lifebuy':
            self.ComboPrice.config(value=self.price_life)
            self.ComboPrice.current(0)    
            self.qty.set(1)  

        if self.ComboProduct.get()=='Lux':
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        if self.ComboProduct.get()=='Santoor':
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0)    
            self.qty.set(1) 

        if self.ComboProduct.get()=='Pearl':
            self.ComboPrice.config(value=self.price_pearl)
            self.ComboPrice.current(0)    
            self.qty.set(1) 

        #face cream
        #Glow&Lovely','Ponds','Olay','Garnier 
        if self.ComboProduct.get()=='Glow&Lovely':
            self.ComboPrice.config(value=self.price_glow)
            self.ComboPrice.current(0)    
            self.qty.set(1)  

        if self.ComboProduct.get()=='Ponds':
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        if self.ComboProduct.get()=='Olay':
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)    
            self.qty.set(1) 

        if self.ComboProduct.get()=='Garnier':
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)    
            self.qty.set(1)  

        #hairoil
        #Parachute','Jashmin','Bajaj
        if self.ComboProduct.get()=='Parachute':
            self.ComboPrice.config(value=self.price_para)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        if self.ComboProduct.get()=='Jashmin':
            self.ComboPrice.config(value=self.price_jashmin)
            self.ComboPrice.current(0)    
            self.qty.set(1) 

        if self.ComboProduct.get()=='Bajaj':
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        #iphone
        #Iphone_X','Iphone_11','Iphone_12
        if self.ComboProduct.get()=='Iphone_X':
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        if self.ComboProduct.get()=='Iphone_11':
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)    
            self.qty.set(1) 

        if self.ComboProduct.get()=='Iphone_12':
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)    
            self.qty.set(1)    
            

        #samsung
        #Samsumg M16','Samsumg M12','Samsung M21
        if self.ComboProduct.get()=='Samsumg M16':
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        if self.ComboProduct.get()=='Samsumg M12':
            self.ComboPrice.config(value=self.price_sm12)
            self.ComboPrice.current(0)    
            self.qty.set(1) 

        if self.ComboProduct.get()=='Samsung M21':
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)    
            self.qty.set(1)   


        #MI
        #Red 11','Readme-12','ReadmePro 
        if self.ComboProduct.get()=='Red 11':
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        if self.ComboProduct.get()=='Readme-12':
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)    
            self.qty.set(1) 

        if self.ComboProduct.get()=='ReadmePro':
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0)    
            self.qty.set(1)     
            
        #real me
        #RealMe  12','RealMe  13','Realme Pro
        if self.ComboProduct.get()=='RealMe  12':
            self.ComboPrice.config(value=self.price_rel12)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        if self.ComboProduct.get()=='RealMe  13':
            self.ComboPrice.config(value=self.price_rel13)
            self.ComboPrice.current(0)    
            self.qty.set(1) 

        if self.ComboProduct.get()=='Realme Pro':
            self.ComboPrice.config(value=self.price_relpro)
            self.ComboPrice.current(0)    
            self.qty.set(1)      


       #one plus
       #OnePlus 1','OnePlus 2','OnePlus 3
        if self.ComboProduct.get()=='OnePlus 1':
            self.ComboPrice.config(value=self.price_one1)
            self.ComboPrice.current(0)    
            self.qty.set(1)

        if self.ComboProduct.get()=='OnePlus 2':
            self.ComboPrice.config(value=self.price_one2)
            self.ComboPrice.current(0)    
            self.qty.set(1) 

        if self.ComboProduct.get()=='OnePlus 3':
            self.ComboPrice.config(value=self.price_one3)
            self.ComboPrice.current(0)    
            self.qty.set(1)     











                  
                        
if __name__=='__main__':
    root= Tk()
    obj=Bill_App(root)
    root.mainloop()     #main page


