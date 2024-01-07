# Nama file : FrmMataKuliah.py
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from MataKuliah import MataKuliah

class FormMataKuliah:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode Mata Kuliah:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtkodemk = Entry(mainFrame) 
        self.txtkodemk.grid(row=0, column=1, padx=5, pady=5) 
        self.txtkodemk.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Nama Mata Kuliah:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtnamamk = Entry(mainFrame) 
        self.txtnamamk.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Jumlah SKS:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtsks = StringVar()
        self.duasks = Radiobutton(mainFrame, text='2 SKS', value='2', variable=self.txtsks)
        self.duasks.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.duasks.select() # set pilihan yg pertama
        self.tigasks = Radiobutton(mainFrame, text='3 SKS', value='3', variable=self.txtsks)
        self.tigasks.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        self.empatsks = Radiobutton(mainFrame, text='4 SKS', value='4', variable=self.txtsks)
        self.empatsks.grid(row=4, column=1, padx=5, pady=5, sticky=W)
  
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'kodemk', 'namamk','sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kodemk', text='Kode Mata Kuliah')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='Nama Mata Kuliah')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='SKS')
        self.tree.column('sks', width="30")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtkodemk.delete(0,END)
        self.txtkodemk.insert(END,"")
        self.txtnamamk.delete(0,END)
        self.txtnamamk.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.duasks.select()
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mk = MataKuliah()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = MataKuliah()
        res = mk.getBykodemk(kodemk)
        rec = mk.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtnamamk.focus()
        return res
        
    def TampilkanData(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = MataKuliah()
        res = mk.getBykodemk(kodemk)
        self.txtkodemk.delete(0,END)
        self.txtnamamk.insert(END,mk.namamk)
        sks = mk.sks
        if(sks=="2"):
            self.duasks.select()
        elif(sks=="3"):
            self.tigasks.select()
        else:
            self.empatsks.select()
        self.txtsks.set(mk.sks)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kodemk = self.txtkodemk.get()
        namamk = self.txtnamamk.get()
        sks = self.txtsks.get()
    
        
        mk = MataKuliah()
        mk.kodemk = kodemk
        mk.namamk = namamk
        mk.sks = sks
        if(self.ditemukan==True):
            res = mk.updateBykodemk(kodemk)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'
            
        rec = mk.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtkodemk.get()
        mk = MataKuliah()
        mk.kodemk = kodemk
        if(self.ditemukan==True):
            res = mk.deleteBykodemk(kodemk)
            rec = mk.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMataKuliah(root, "Aplikasi Mata Kuliah")
    root.mainloop() 