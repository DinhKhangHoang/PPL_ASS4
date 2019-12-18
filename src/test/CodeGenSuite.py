import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
#     def test_int(self):
#         """Simple program: int main() {} """
#         input = """void main() {putInt(100);}"""
#         expect = "100"
#         self.assertTrue(TestCodeGen.test(input,expect,500))
#     def test_int_ast(self):
#     	input = Program([
#     		FuncDecl(Id("main"),[],VoidType(),Block([
#     			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
#     	expect = "5"
#     	self.assertTrue(TestCodeGen.test(input,expect,501))
#     def test_02(self):
#         input = """int b[9];
#         float c;
#         void main() {
#             int d[10];
#             putInt(100);
#             float e;
#             putFloat(5.2);
#         }
#         """
#         expect = "1005.2"
#         self.assertTrue(TestCodeGen.test(input,expect,502))

#     def test_03(self):
#         input = """int b[9];
#         float c;
#         void main() {
#             int d[10];
#             putInt(100);
#         }
#         """
#         expect = "100"
#         self.assertTrue(TestCodeGen.test(input,expect,503))
#     def test_04(self):
#         input = """int b[9];
#         float c;
#         void main() {
#             int d[10];
#             putInt(100);
#             {
#                 7;
#                 int e[5];
#                 8;
#             }
#         }
#         """
#         expect = "100"
#         self.assertTrue(TestCodeGen.test(input,expect,504))

#     def test_05(self):
#         input = """int b[9];
#         float c;
#         void main() {
#             int d[10];
#             if(true){
#                 putInt(5);
#             }
#             else{
#                 putFloat(5.2);
#             }
#         }
#         """
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,505))

#     def test_06(self):
#         input = """int b[9];
#         float c;
#         void main() {
#             int d[10];
#             if(false){
#                 putInt(5);
#             }
#             else{
#                 putFloat(5.2);
#             }
#         }
#         """
#         expect = "5.2"
#         self.assertTrue(TestCodeGen.test(input,expect,506))

#     def test_07(self):
#         input = """int b[9];
#         float c;
#         void main() {
#             int d[10];
#             if(false){
#                 putInt(5);
#             }
#             else{
#                 putFloat(5.2);
#             }
#         }
#         """
#         expect = "5.2"
#         self.assertTrue(TestCodeGen.test(input,expect,507))

#     def test_08(self):
#         input = """int b[9];
#         float c;
#         void main() {
#             if(false){
#                 c;
#                 putInt(5);
#             }
#             else{
#                 putFloat(5.2);
#             }
            
#         }
#         """
#         expect = "5.2"
#         self.assertTrue(TestCodeGen.test(input,expect,508))

#     def test_09(self):
#         input = """int b[9];
#         float c;
#         void main() {
#             boolean b;
#             b = true;
#             if(b){
#                 c;
#                 putInt(5);
#             }
#             else{
#                 putFloat(5.2);
#             }
            
#         }
#         """
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,509))

#     def test_10(self):
#         input = """int b[9];
#         float c;
#         void main() {
#             boolean b, c;
#             b = true;
#             c = false;
#             b = b || c;
#             if(b){
#                 c;
#                 putInt(5);
#             }
#             else{
#                 putFloat(5.2);
#             }
            
#         }
#         """
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,510))

#     def test_11(self):
#         input = """int b[9];
#         float c;
#         void main() {
#             boolean b, c;
#             b = true;
#             c = false;
#             b = b && c;
#             if(b){
#                 c;
#                 putInt(5);
#             }
#             else{
#                 putFloat(5.2);
#             }
            
#         }
#         """
#         expect = "5.2"
#         self.assertTrue(TestCodeGen.test(input,expect,511))

#     def test_12(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
            
#         }
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,512))

#     def test_13(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             boolean e[2];
#         }
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,513))

#     def test_14(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             {
#                 boolean e[2];
#             }
#         }
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,514))

#     def test_vardecl_in_many_scope(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             {
#                 boolean e[2];
#                 {
#                     int a[5];
#                 }
#             }
#         }
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,515))

#     def test_vardecl_in_many_scope2(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             {
#                 boolean e[2];
#                 {
#                     int a[5];
#                 }
#                 {
#                     string f[2];
#                 }
#             }
#         }
#         """
#         expect = ""
#         self.assertTrue(TestCodeGen.test(input,expect,516))

#     def test_gencode_for_if(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             if(true){
#                 if(false)
#                    putIntLn(34);
#             }
#             else{
#                 putInt(5);
#             }
#             putFloat(7.8);
#         }
#         """
#         expect = "7.8"
#         self.assertTrue(TestCodeGen.test(input,expect,517))

#     def test_gencode_for_if2(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             if(true){
#                 if(false)
#                    putIntLn(34);
#                 else{
#                     putFloatLn(5.6);
#                 }
#             }
#             else{
#                 putInt(5);
#             }
#             putFloat(7.8);
#         }
#         """
#         expect = """5.6
# 7.8"""
#         self.assertTrue(TestCodeGen.test(input,expect,518))

#     def test_gencode_for_if3(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             if(true){
#                 if(false)
#                    putIntLn(34);
#                 else{
#                     if(true){
#                         putString("khang goes pro");
#                     }
#                     else{
#                         putString("khang cant go pro");
#                     }
#                 }
#             }
#             else{
#                 putInt(5);
#             }
#             putFloat(7.8);
#         }
#         """
#         expect = "khang goes pro7.8"
#         self.assertTrue(TestCodeGen.test(input,expect,519))

#     def test_gencode_for_if4(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             if(true){
#                 if(false)
#                    putIntLn(34);
#                 else{
#                     if(true){
#                         putString("khang goes pro");
#                     }
#                     else{
#                         putString("khang cant go pro");
#                     }
#                 }
#             }
#             else{
#                 putInt(5);
#             }
#             putFloat(7.8);
#         }
#         """
#         expect = "khang goes pro7.8"
#         self.assertTrue(TestCodeGen.test(input,expect,520))

#     def test_gencode_for_if5(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             if(false){
#                 if(false)
#                    putIntLn(34);
#                 else{
#                     if(true){
#                         putString("khang goes pro");
#                     }
#                     else{
#                         putString("khang cant go pro");
#                     }
#                 }
#             }
#             else{
#                 putInt(5);
#                 if(true)
#                     putFloat(8.9);
#                 if(false){
#                     putInt(10);
#                 }
#                 else{
#                     putFloat(1011);
#                 }
#             }
#             putFloat(7.8);
#         }
#         """
#         expect = "58.91011.07.8"
#         self.assertTrue(TestCodeGen.test(input,expect,521))

#     def test_gencode_for_if6(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             if(false){
#                 if(false)
#                    putIntLn(34);
#                 else{
#                     if(true){
#                         putString("khang goes pro");
#                     }
#                     else{
#                         putString("khang cant go pro");
#                     }
#                 }
#             }
#             else{
#                 putInt(5);
#                 if(true)
#                     putFloat(8.9);
#                 if(true){
#                     if(false)
#                         putInt(10);
#                     else
#                         putFloat(13);
#                 }
#                 else{
#                     putFloat(1011);
#                 }
#             }
#             putFloat(7.8);
#         }
#         """
#         expect = "58.913.07.8"
#         self.assertTrue(TestCodeGen.test(input,expect,522))

#     def test_gencode_for_forstmt(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             int i, a;
#             a = 1;
#             for(i = 1 ; i < 10; i = i + 1){
#                 a = a * i;
#             }
#             putInt(a);
#         }
#         """
#         expect = "362880"
#         self.assertTrue(TestCodeGen.test(input,expect,523))

#     def test_gencode_for_forstmt1(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             int i, a;
#             a = 1;
#             for(i = 1 ; i < 10; i = i + 1){
#                 //a = a * i;
#             }
#             putInt(a);
#         }
#         """
#         expect = "1"
#         self.assertTrue(TestCodeGen.test(input,expect,524))

#     def test_gencode_for_forstmt2(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             int i, j, a;
#             a = 1;
#             for(i = 0 ; i < 10; i = i + 1){
#                 for(j = 1 ; j < 10; j = j +1){
#                     a = a + j;
#                 }
#             }
#             putInt(a);
#         }
#         """
#         expect = "451"
#         self.assertTrue(TestCodeGen.test(input,expect,525))

#     def test_gencode_for_forstmt3(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             int i, j, a;
#             a = 1;
#             for(i = 1 ; i < 10; i = i + 1){
#                 for(j = 1 ; j < 10; j = j +1){
#                     a = a + j;
#                 }
#                 for(j = 1; j < 10; j = j + 1)
#                     a = a + j;
#             }
#             putInt(a);
#         }
#         """
#         expect = "811"
#         self.assertTrue(TestCodeGen.test(input,expect,526))

#     def test_gencode_for_forstmt4(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             int i, j, a;
#             a = 1;
#             for(i = 1 ; i < 10; i = i + 1){
#                 for(j = 1 ; j < 10; j = j +1){
#                     a = a + j;
#                 }
#             }
#             for(j = 1; j < 10; j = j + 1)
#                 a = a + j;
#             putInt(a);
#         }
#         """
#         expect = "451"
#         self.assertTrue(TestCodeGen.test(input,expect,527))

#     def test_gencode_for_forstmt5(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             int i, j, a;
#             a = 1;
#             for(i = 1 ; i < 10; i = i + 1){
#                 for(j = 1 ; j < 10; j = j +1){
#                     a = a + j;
#                 }
#             }
#             for(i = 1 ; i < 10; i = i + 1){
#                 for(j = 1 ; j < 10; j = j +1){
#                     a = a + j;
#                 }
#             }
#             putInt(a);
#         }
#         """
#         expect = "811"
#         self.assertTrue(TestCodeGen.test(input,expect,528))

#     def test_gencode_for_forstmt6(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             int i, j, a;
#             a = 1;
#             for(i = 1 ; i < 10; i = i + 1){
#                 for(j = 1 ; j < 10; j = j +1){
#                     a = a + j;
#                 }
#             }
#             for(i = 1 ; i < 10; i = i + 1){
#                 for(j = 1 ; j < 10; j = j +1){
#                     a = a + j;
#                 }
#             }
#             putInt(a);
#         }
#         """
#         expect = "811"
#         self.assertTrue(TestCodeGen.test(input,expect,529))

#     def test_gencode_for_dowhilestmt(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             int i, j, a;
#             a = 1;
#             i = 0;
#             do{
#                 a = a + i;
#                 i = i + 1;
#             }while(i <= 10);
#             putInt(a);
#         }
#         """
#         expect = "56"
#         self.assertTrue(TestCodeGen.test(input,expect,530))

#     def test_gencode_for_dowhilestmt1(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             int i, j, a;
#             a = 1;
#             i = 0;
#             do{
#                 a = a + i;
#                 i = i + 1;
#             }while(i <= 10);
#             do{
#                 a = a + i;
#                 i = i + 1;
#             }while(i <= 10);
#             putInt(a);
#         }
#         """
#         expect = "67"
#         self.assertTrue(TestCodeGen.test(input,expect,531))

#     def test_gencode_for_dowhilestmt2(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             int i, j, a;
#             a = 1;
#             i = 0;
#             do{
#                 a = a + i;
#                 i = i + 1;
#                 j = 0;
#                 do{
#                     a = a + i;
#                     j = j + 1;
#                 }while(j <= 10);
#             }while(i <= 10);
            
#             putInt(a);
#         }
#         """
#         expect = "782"
#         self.assertTrue(TestCodeGen.test(input,expect,532))

#     def test_gencode_for_dowhilestmt3(self):
#         input = """int b[9];
#         float c;
#         float d[10];
#         void main() {
#             int i, j, a;
#             a = 1;
#             i = 0;
#             do{
#                 a = a + i;
#                 i = i + 1;
#                 j = 0;
#                 do{
#                     int k;
#                     k = 0;
#                    do{
#                        a = a + 1;
#                        k = k + 1;
#                    }while(k <= 10);
#                     j = j + 1;
#                 }while(j <= 10);
#             }while(i <= 10);
            
#             putInt(a);
#         }
#         """
#         expect = "1387"
#         self.assertTrue(TestCodeGen.test(input,expect,533))

#     def test_gencode_for_dowhilestmt4(self):
#         input = """int a, b;
#         void main(){
#             a = 0;
#             b = 8;
#             float f;
#             f = 7.8;
#             do{
#                 do{
#                     f = f + 1;
#                 }while(f < 10);
#             }while(false);
#             putFloat(f);
#         }
#         """
#         expect = "10.8"
#         self.assertTrue(TestCodeGen.test(input,expect,534))

#     def test_gencode_for_dowhilestmt5(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 0;
#             do{
#                 c[i] = i;
#                 i = i + 1;
#             }while(i < 10);
#             putInt(c[7]);
#         }
#         """
#         expect = "7"
#         self.assertTrue(TestCodeGen.test(input,expect,535))

#     def test_gencode_for_for35(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 0;
#             for(i = 0; i < 10; i = i + 1)
#                 c[i] = i*i;
#             putInt(c[7]);
#         }
#         """
#         expect = "49"
#         self.assertTrue(TestCodeGen.test(input,expect,536))

#     def test_gencode_for_dowhile7(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             do{
#                 c[i] = i;
#                 i = i - 1;
#             }while(i >= 0);
#             putInt(c[5]);
#         }
#         """
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,537))

#     def test_gencode_for_dowhile8(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             do{
#                 c[i] = i*i;
#                 i = i - 1;
#             }while(i >= 0);
#             putInt(c[5] + c[6] + c[7]);
#         }
#         """
#         expect = "110"
#         self.assertTrue(TestCodeGen.test(input,expect,538))

#     def test_gencode_for_break(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             do{
#                 c[i] = i*i;
#                 i = i - 1;
#                 break;
#             }while(i >= 0);
#             putInt(i);
#         }
#         """
#         expect = "8"
#         self.assertTrue(TestCodeGen.test(input,expect,539))

#     def test_gencode_for_break1(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             do{
#                 i = i - 1;
#                 if (i < 5)
#                     break;
#             }while(i >= 0);
#             putInt(i);
#         }
#         """
#         expect = "4"
#         self.assertTrue(TestCodeGen.test(input,expect,540))
    
#     def test_gencode_for_break2(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             do{
#                 do{
#                     i = i -1;
#                 }while(i > 5);
#                 break;
#             }while(i >= 0);
#             putInt(i);
#         }
#         """
#         expect = "5"
#         self.assertTrue(TestCodeGen.test(input,expect,541))
    
#     def test_gencode_for_break3(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             do{
#                 do{
#                     i = i -1;
#                     if(true)
#                         break;
#                 }while(i > 5);
#                 i = i -1;
#             }while(i >= 0);
#             putInt(i);
#         }
#         """
#         expect = "-1"
#         self.assertTrue(TestCodeGen.test(input,expect,542))
    
#     def test_gencode_for_break4(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             do{
#                 do{
#                     i = i -1;
#                     if(true)
#                         break;
#                 }while(i > 5);
#                 do{
#                     i = i -1;
#                     if(true)
#                         break;
#                 }while(i > 5);
#             }while(i >= -1);
#             putInt(i);
#         }
#         """
#         expect = "-3"
#         self.assertTrue(TestCodeGen.test(input,expect,543))
    
#     def test_gencode_for_break5(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             do{
#                 do{
#                     do{
#                         i = i -1;
#                         if(true)
#                             break;
#                     }while(i > 5);
#                     i = i -1;
#                     if(true)
#                         break;
#                 }while(i > 5);
#                 i = i -1;
#             }while(i >= 0);
#             putInt(i);
#         }
#         """
#         expect = "-3"
#         self.assertTrue(TestCodeGen.test(input,expect,544))
    
#     def test_gencode_for_break6(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             do{
#                 do{
#                     do{
#                         i = i -1;
#                         if(true)
#                             break;
#                     }while(i > 5);
#                     i = i -1;
#                     if(true)
#                         break;
#                 }while(i > 5);
#                 do{
#                     i = i -1;
#                     if (true)
#                         break;
#                 }while(i > 5);
#                 i = i -1;
#             }while(i >= 0);
#             putInt(i);
#         }
#         """
#         expect = "-3"
#         self.assertTrue(TestCodeGen.test(input,expect,545))
    
#     def test_gencode_for_continue(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             for(i = 0; i < 10; i = i + 1){
#                 c[i] = 10 - i;
#                 if(true)
#                     continue;
#             }
#             putInt(i);
#         }
#         """
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,546))
    
#     def test_gencode_for_continue1(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             for(i = 0; i < 10; i = i + 1){
#                 c[i] = 10 - i;
#                 if(i < 5){
#                     c[i] = c[i] * 2;
#                     continue;
#                 }
#                 continue;
#             }
#             putInt(i);
#         }
#         """
#         expect = "10"
#         self.assertTrue(TestCodeGen.test(input,expect,547))
    
#     def test_gencode_for_continue2(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             for(i = 0; i < 10; i = i + 1){
#                 c[i] = 10 - i;
#                 if(i < 5){
#                     continue;
#                 }
#                 c[i] = c[i] * 3;
#             }
#             putInt(c[9]);
#         }
#         """
#         expect = "3"
#         self.assertTrue(TestCodeGen.test(input,expect,548))
    
#     def test_gencode_for_continue3(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             for(i = 0; i < 10; i = i + 1){
#                 c[i] = 10 - i;
#                 int j;
#                 for(j = 0; j < 10; j = j + 1){
#                     if(j < 5){
#                         continue;
#                     }
#                     c[j] = c[j] * 4;
#                 }
                
#             }
#             putInt(c[9]);
#         }
#         """
#         expect = "4"
#         self.assertTrue(TestCodeGen.test(input,expect,549))
    
#     def test_gencode_for_continue50(self):
#         input = """int a, b;
#         void main(){
#             int c[10];
#             int i;
#             i = 9;
#             for(i = 0; i < 10; i = i + 1){
#                 c[i] = 10 - i;
#                 int j;
#                 for(j = 0; j < 10; j = j + 1){
#                     if(j < 5){
#                         continue;
#                     }
#                     c[j] = c[j] * 4;
#                 }
                
#             }
#             putInt(c[9]);
#         }
#         """
#         expect = "4"
#         self.assertTrue(TestCodeGen.test(input,expect,550))
    
    

#     def test_use_var_glo_vs_var_loc(self):
#         input = """
#         int a;
#         void main() {
#             a = 1;
#             {
#                 putInt(a);
#                 int a;
#                 a = 2;
#                 putInt(a);
#             }
#             putInt(a);
#         }
#         """
#         expect = """121"""
#         self.assertTrue(TestCodeGen.test(input, expect, 576))

#     def test_bubblesort(self):
#         input = """
#         void main() {
#             int a[5];
#             int i;
#             for (i=0;i<5;i=i+1){
#                 a[i] = 5-i;
#             }
#             int j;
#             for (j=0;j<5;j = j+1){
#                 for (i=0;i<4;i=i+1){
#                     if (a[i] > a[i+1]){
#                         int tmp;
#                         tmp = a[i];
#                         a[i] = a[i+1];
#                         a[i+1] = tmp;
#                     }
#                 }
#             }
#             for (i=0;i<5;i=i+1){
#                 putInt(a[i]);
#             }
#         }
#         """
#         expect = """12345"""
#         self.assertTrue(TestCodeGen.test(input, expect, 577))

#     def test_fibo_recur(self):
#         input = """
#         int fibo(int n) {
#             if (n == 1) return 1;
#             if (n == 0) return 0;
#             return fibo(n-1) + fibo(n-2);
#         }
#         void main() {
#             putInt(fibo(5));
#         }
#         """
#         expect = """5"""
#         self.assertTrue(TestCodeGen.test(input, expect, 578))

#     def test_print_str(self):
#         input = """
#         string helo() {
#             string a;
#             a = "helo bac si";
#             return a;
#         }
#         void main() {
#             putString(helo());
#         }
#         """
#         expect = """helo bac si"""
#         self.assertTrue(TestCodeGen.test(input, expect, 579))

#     def test_dowhile_assign_var(self):
#         input = """
#         void main() {
#             int a,b;
#             a = 2;
#             b = 2;
#             a + b;
#             do {
#                 int a;
#                 a = 3;
#             } while (a - b != 0);
#         }
#         """
#         expect = """"""
#         self.assertTrue(TestCodeGen.test(input, expect, 580))

#     def test_mix_up_assign_op(self):
#         input = """
#         void main() {
#             int a;
#             float b;
#             b = 2;
#             putFloat(b);
#         }
#         """
#         expect = """2.0"""
#         self.assertTrue(TestCodeGen.test(input, expect, 581))

#     def test_assign_in_exp(self):
#         input = """
#         void main() {
#             int a;
#             float b;
#             a = 1;
#             2 + (2);
#             a = 2;
#             putInt(a);
#         }
#         """
#         expect = """2"""
#         self.assertTrue(TestCodeGen.test(input, expect, 582))

#     def test_assign_in_exp_w_shortcut(self):
#         input = """
#         void main() {
#             int a, c;
#             float b;
#             a = 1;
#             true || a + (2) > 0;
#             a = 2;
#             b = 2;
#             putInt(a);
#         }
#         """
#         expect = """2"""
#         self.assertTrue(TestCodeGen.test(input, expect, 583))

#     def test_much_array(self):
#         input = """
#         int a[5];
#         string b[5];
#         float c[5];
#         boolean d[5];
#         void main() {
#             int a[5];
#             string b[5];
#             float c[5];
#             boolean d[5];
#         }
#         """
#         expect = """"""
#         self.assertTrue(TestCodeGen.test(input, expect, 584))

#     def test_assign_intcell_to_float_cell(self):
#         input = """
#         int a[5];
#         string b[5];
#         float c[5];
#         boolean d[5];
#         void main() {
#             a[1] = 2;
#             c[1] = a[1];
#             putFloat(c[1]);
#         }
#         """
#         expect = """2.0"""
#         self.assertTrue(TestCodeGen.test(input, expect, 585))

#     def test_print_assign_param(self):
#         input = """
#         int a[5];
#         string b[5];
#         float c[5];
#         boolean d[5];
#         void main() {
#             putFloat(3);
#         }
#         """
#         expect = """3.0"""
#         self.assertTrue(TestCodeGen.test(input, expect, 586))

#     def test_assign_unop(self):
#         input = """
#         int a[5];
#         string b[5];
#         float c[5];
#         boolean d[5];
#         void main() {
#             c[1] = 3;
#             putFloat(c[1]);
#         }
#         """
#         expect = """3.0"""
#         self.assertTrue(TestCodeGen.test(input, expect, 587))

#     def test_assign_bitop(self):
#         input = """
#         int a[5];
#         string b[5];
#         float c[5];
#         boolean d[5];
#         void main() {
#             d[1] = true;
#             (d[1]) && false;
#             putBool(d[1]);
#         }
#         """
#         expect = """true"""
#         self.assertTrue(TestCodeGen.test(input, expect, 588))

#     def test_assign_w_reop(self):
#         input = """
#         int a[5];
#         string b[5];
#         float c[5];
#         boolean d[5];
#         void main() {
#             a[1] = 2;
#             (a[1]) > 2;
#             putInt(a[1]);
#         }
#         """
#         expect = """2"""
#         self.assertTrue(TestCodeGen.test(input, expect, 589))

#     def test_program_w_print(self):
#         input = """
#         void print(int a) {
#             putInt(a);
#         }
#         void main() {
#             print(1);
#         }
#         """
#         expect = """1"""
#         self.assertTrue(TestCodeGen.test(input, expect, 590))

#     def test_pro_w_add(self):
#         input = """
#         void print(int a) {
#             putInt(a);
#         }
#         int add(int a, int b) {
#             return a + b;
#         }
#         void main() {
#             print(add(159, 753));
#         }
#         """
#         expect = """912"""
#         self.assertTrue(TestCodeGen.test(input, expect, 591))

#     def test_pro_w_div(self):
#         input = """
#         void print(int a) {
#             putInt(a);
#         }
#         int add(int a, int b) {
#             return a + b;
#         }
#         int div(int a, int b) {
#             return a/b;
#         }
#         void main() {
#             print(div(add(159, 753),2));
#         }
#         """
#         expect = """456"""
#         self.assertTrue(TestCodeGen.test(input, expect, 592))

#     def test_pro_w_mod(self):
#         input = """
#         void print(int a) {
#             putInt(a);
#         }
#         int add(int a, int b) {
#             return a + b;
#         }
#         int div(int a, int b) {
#             return a/b;
#         }
#         int mod(int a, int b) {
#             return a%b;
#         }
#         void main() {
#             print(mod(div(add(159, 753),2),2));
#         }
#         """
#         expect = """0"""
#         self.assertTrue(TestCodeGen.test(input, expect, 593))

#     def test_pro_check_prime(self):
#         input = """
#         boolean isPrim(int a) {
#             if (a <= 1) return false;
#             int i;
#             for (i = 2; i < a/2+1; i=i+1) {
#                 if (a%i==0) return false;
#             }
#             return true;
#         }
#         void main() {
#             putBool(isPrim(137));
#         }
#         """
#         expect = """true"""
#         self.assertTrue(TestCodeGen.test(input, expect, 594))

#     def test_pro_check_gcd(self):
#         input = """
#         int gcd(int a, int b) {
#             if (b == 0) return a;
#             return gcd(b, a%b);
#         }
#         void main() {
#             putInt(gcd(6,10));
#         }
#         """
#         expect = """2"""
#         self.assertTrue(TestCodeGen.test(input, expect, 595))

#     def test_pro_check_lcm(self):
#         input = """
#         int lcm(int a, int b) {
#             return a*b/gcd(a,b);
#         }
#         int gcd(int a, int b) {
#             if (b == 0) return a;
#             return gcd(b, a%b);
#         }
#         void main() {
#             putInt(lcm(6,10));
#         }
#         """
#         expect = """30"""
#         self.assertTrue(TestCodeGen.test(input, expect, 596))

#     def test_pro_checksum(self):
#         input = """
#         int checksum(int a[]) {
#             int sum, i;
#             sum = 0;
#             for (i = 0; i < 10; i = i + 1) {
#                 sum = sum + a[i];
#             }
#             return sum;
#         }
#         int a[10];
#         void main() {
#             a[1] = 1;
#             a[2] = 2;
#             putInt(checksum(a));
#         }
#         """
#         expect = """3"""
#         self.assertTrue(TestCodeGen.test(input, expect, 597))

#     def test_pro_xor(self):
#         input = """
#         boolean xor(boolean a, boolean b) {
#             return a != b;
#         }
#         void main() {
#             putBool(xor(true, false));
#         }
#         """
#         expect = """true"""
#         self.assertTrue(TestCodeGen.test(input, expect, 598))

#     def test_pro_feel_good(self):
#         input = """
#         boolean feel(int a) {
#             if (a > 0) return true;
#             return false;
#         }
#         boolean good(int a) {
#             if (a*a-a+a/a%a == 0) return true;
#             return false;
#         }
#         void main() {
#             putBool(feel(0) || good(-1));
#         }
#         """
#         expect = """false"""
#         self.assertTrue(TestCodeGen.test(input, expect, 599))

#     def test_value_complex_program_No1(self):
#         input = """
#         int f()
#         {
#             return 200;
#         }
#         void main(){
#             int main;
#             main = f();
#             putIntLn(main);
#             {
#                 int i;
#                 int main;
#                 int f;
#                 main = 100;
#                 i = main;
#                 f = main;
#                 putIntLn(i);
#                 putIntLn(main);
#                 putIntLn(f);
#             }
#             putIntLn(main);
#         }
#         """
#         expect = """200\n100\n100\n100\n200\n"""
#         self.assertTrue(TestCodeGen.test(input, expect, 600))

    # def test_print_global_var_int_type(self):
    #     input = """
    #     int a;
    #     void main()
    #     {
    #         putInt(a);
    #     }
    #     """
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))

    # def test_print_global_var_float_type(self):
    #     input = """
    #     float a;
    #     void main()
    #     {
    #         putFloatLn(a);
    #     }
    #     """
    #     expect = "0.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))

    # def test_print_global_var_boolean_type(self):
    #     input = """
    #     boolean a;
    #     void main()
    #     {
    #         putBool(a);
    #     }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))

    # def test_print_global_var_array_int_type(self):
    #     input = """
    #     int a[1];
    #     void main()
    #     {
    #         putInt(a[0]);
    #     }
    #     """
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))

    # def test_print_global_var_array_float_type(self):
    #     input = """
    #     float a[1];
    #     void main()
    #     {
    #         putFloatLn(a[0]);
    #     }
    #     """
    #     expect = "0.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))

    # def test_value_add_sub_neg_assign_op_for_int(self):
    #     input = """
    #     void main()
    #     {
    #         int a;
    #         a = 1+(-2)-(-6)+2;
    #         putIntLn(a);
    #     }
    #     """
    #     expect = "7\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))

    # def test_value_add_sub_op_for_float(self):
    #     input = """
    #     void main()
    #     {
    #         float a;
    #         a = 2-8+9-10;
    #         putFloat(a);
    #     }
    #     """
    #     expect = "-7.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))

    # def test_value_mul_div_op_for_int(self):
    #     input = """
    #     void main()
    #     {
    #         int a;
    #         a = 2*7*9/5;
    #         putIntLn(a);
    #     }
    #     """
    #     expect = "25\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))

    # def test_value_mul_div_op_for_float(self):
    #     input = """
    #     void main()
    #     {
    #         float a;
    #         a = 2*7*9.0/11;
    #         putFloat(a);
    #     }
    #     """
    #     expect = "11.454545"
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))

    # def test_value_mul_div_mod_for_int(self):
    #     input = """
    #     void main()
    #     {
    #         int a;
    #         a = 10*10*10*10/100%10*10;
    #         putIntLn(a);
    #     }
    #     """
    #     expect = "0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))

    # def test_value_greater_than_op_in_int(self):
    #     input = """
    #     void main()
    #     {
    #         boolean a;
    #         a = 2>3;
    #         putBool(a);
    #     }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))

    # def test_value_less_than_op_in_float(self):
    #     input = """
    #     void main()
    #     {
    #         boolean a;
    #         a = 2.0<8.0;
    #         putBool(a);
    #     }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))

    # def test_value_ge_op_in_float(self):
    #     input = """
    #     void main()
    #     {
    #         boolean a;
    #         a = 8>=8.0;
    #         putBool(a);
    #     }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))

    # def test_value_reop_and_op_eval_1(self):
    #     input = """
    #     void main()
    #     {
    #         boolean c;
    #         c = (2<3) && (2>3);
    #         putBool(c);
    #     }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))

    # def test_value_and_op_eval_2(self):
    #     input = """
    #     void main()
    #     {
    #         boolean c;
    #         int a;
    #         a = 9;
    #         c = (2>3) && a/0 > 0;
    #         putBool(c);
    #     }
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))

    # def test_value_or_op_eval_1(self):
    #     input = """
    #     void main()
    #     {
    #         boolean c;
    #         c = (2<3) || (2>3);
    #         putBool(c);
    #     }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))

    # def test_value_or_op_eval_2(self):
    #     input = """
    #     void main()
    #     {
    #         boolean c;
    #         int a;
    #         a = 9;
    #         c = (2<3) || a/0 > 0;
    #         putBool(c);
    #     }
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))

    # def test_value_eq_op_and_not_eq_for_int(self):
    #     input = """
    #     void main()
    #     {
    #         boolean c;
    #         int a;
    #         a = 2;
    #         c= a==a;
    #         putBoolLn(c);
    #         c = a!=a;
    #         putBool(c);

    #     }
    #     """
    #     expect = """true\nfalse"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))

    # def test_value_neg_num(self):
    #     input = """
    #     void main()
    #     {
    #         boolean c;
    #         int a;
    #         a = 3;
    #         c = -a >-3;
    #         putBool(c);

    #     }
    #     """
    #     expect = """false"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_value_not_exp(self):
        input = """
        void main()
        {
            boolean c;
            int a;
            a = 3;
            c = !(-a >-3);
            putBool(c);

        }
        """
        expect = """true"""
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    # def test_value_complex_exp_global_No1(self):
    #     input = """
    #     int a;
    #     void main()
    #     {
    #         float c;
    #         c = a + 2 - 1 * 6.0/ 4.0;
    #         putFloat(c);
    #     }
    #     int b;
    #     """
    #     expect = """0.5"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))

    # def test_value_not_exp_No2(self):
    #     input = """
    #     boolean a,b,c;
    #     void main()
    #     {
    #        c = true;
    #        b = true;
    #        a = b || c;
    #        putBoolLn(a);
    #        putBoolLn(b && false);
    #        putBoolLn(false || c);

    #     }
    #     """
    #     expect = """true\nfalse\ntrue\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))

    # def test_value_many_assign_op_No1(self):
    #     input = """
    #     void main()
    #     {
    #         int a,b,c;
    #         a = b= c = 1;
    #         putInt(a);putInt(b); putInt(c);
    #     }
    #     """
    #     expect = """111"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))

    # def test_value_many_assign_op_No2(self):
    #     input = """
    #     void main()
    #     {
    #         int a[3];
    #         a[1]=a[2]=a[0] = 8;
    #         putInt(a[1]*a[2]+a[0]);
    #     }
    #     """
    #     expect = """72"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))

    # def test_value_exp_w_arraycell_No1(self):
    #     input = """
    #     void main()
    #     {
    #         int a[3];
    #         a[1]=a[2]=a[0] = 8;
    #         int b;
    #         int c;
    #         int d[2];
    #         b=1;
    #         d[b] = a[2]*a[b];
    #         d[b-1] = a[2] * b;
    #         putIntLn(d[b]);
    #         putIntLn(d[b-1]);  
    #     }
    #     """
    #     expect = """64\n8\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))

    # def test_value_exp_w_arraycell_No2(self):
    #     input = """
    #     void main()
    #     {
    #         int a[3];
    #         a[1]=a[2]=a[0] = 8;
    #         int b;
    #         int c;
    #         float d[2];
    #         b=0;
    #         d[b] = a[2]*2.0/a[b];
    #         d[b+1] = a[2] * b;
    #         putFloatLn(d[b]);
    #         putFloatLn(d[b+1]);  
    #     }
    #     """
    #     expect = """2.0\n0.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))

    # def test_value_exp_w_arraycell_No3(self):
    #     input = """
    #     boolean b[3];
    #     void main()
    #     {
    #         boolean d[2];
    #         d[1] = true;
    #         d[0] = false;
    #         d[0] = b[1] || d[1];
    #         d[1] = (3 == 7) && 6>5;
    #         putBoolLn(d[1]);
    #         putBoolLn(d[0] && true);
    #     }
    #     """
    #     expect = """false\ntrue\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 527))

    # def test_value_complex_exp_No1(self):
    #     input = """
    #     void main()
    #     {
    #         int a; 
    #         float b;
    #         b = a = 0;
    #         b = a*b - 9 + 10*b;
    #         putFloat(b);
    #     }
        
    #     """
    #     expect = """-9.0"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 528))

    # def test_value_complex_exp_No2(self):
    #     input = """
    #     void main()
    #     {
    #         int a; 
    #         float b;
    #         a = 20%3 + 6 -10*19 + 34;
    #         b = a*79 + 90 -89.0/234;
    #         putFloat(b);
    #     }
        
    #     """
    #     expect = """-11602.38"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 529))

    # def test_value_complex_exp_No3(self):
    #     input = """
    #     void main()
    #     {
    #         boolean a,b;
    #         int c,d;
    #         c = 3; d = 10;
    #         a = 8 < 9 || 9>10 && 0<-1;
    #         b = a && (c>d) || 10/6 > 5;
    #         putBoolLn(a);
    #         putBool(b);
    #     }
        
    #     """
    #     expect = """true\nfalse"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 530))

    # def test_value_call_func_No1(self):
    #     input = """
    #     int foo1()
    #     {
    #         return 2;
    #     }
    #     int foo2()
    #     {
    #         return 4;
    #     }
    #     void main()
    #     {
    #         int a,b;
    #         a = foo1();
    #         b = foo2();
    #         int c;
    #         c = a+ b;
    #         putIntLn(c);
    #     }
        
    #     """
    #     expect = """6\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 531))

    # def test_value_call_func_No2(self):
    #     input = """
    #     int foo(int a)
    #     {
    #         return a;
    #     }
    #     void main()
    #     {
    #         putInt(foo(foo(foo(foo(foo(1)+5)+4)+3)+2));
    #     }
    #     """
    #     expect = """15"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 532))

    # def test_value_call_func_No3(self):
    #     input = """
    #     int foo(int a)
    #     {
    #         return a;
    #     }
    #     void main()
    #     {
    #         putInt(foo(foo(foo(foo(foo(1)+5)+4)+3)+2));
    #     }
    #     """
    #     expect = """15"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 533))

    # def test_value_call_func_No4(self):
    #     input = """
    #     int[] foo(int a[])
    #     {
    #         return a;
    #     }
    #     void main(){
    #         int a[3];
    #         a[0] = 1;
    #         putFloat(foo(a)[0]);
    #        }
    #     """
    #     expect = """1.0"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 534))

    # def test_value_call_func_No5(self):
    #     input = """
    #     float[] foo(float a[])
    #     {
    #         a[2] = 9;
    #         return a;
    #     }
    #     void main(){
    #         float a[3];
    #         a[0] = 1;
    #         foo(a);
    #         putFloat(foo(a)[0]+ foo(a)[2]);
    #        }
    #     """
    #     expect = """10.0"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 534))

    # def test_value_call_func_No6(self):
    #     input = """
    #     void haha(string a[], int c){
    #         putString(a[0]);
    #         putInt(c);   
    #     }
    #         void main(){
    #             string c[1];
    #             c[0] = "So nguyen da co ne : ";
    #             haha(c,1+2);
    #        }
    #     """
    #     expect = """So nguyen da co ne : 3"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 535))

    # def test_value_call_func_No7(self):
    #     input = """
    #     void haha(int a, int b)
    #     {
    #         putInt(a+b);
    #     }
    #     void main(){
    #         haha(1+2, 5);
    #        }
    #     """
    #     expect = """8"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 536))

    # def test_value_call_func_No8(self):
    #     input = """
    #     void haha(int a[], int c){
    #         putInt(c);
    #     }
    #     int[] foo()
    #         { 
    #             int a[5];
    #             return a;
    #         }
    #         void main(){
    #             haha(foo(),1+2);
    #        }
    #     """
    #     expect = """3"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 537))

    # def test_block_stmt_global_var(self):
    #     input = """
    #     int a;
    #     void main()
    #     {
    #         putIntLn(a);
    #         int a;
    #         a = 1;
    #         putIntLn(a);
    #         {
    #             int a;
    #             a = 2;
    #             putIntLn(a);
    #             {
    #                 int a;
    #                 a = 3;
    #                 putIntLn(a);
    #             }
    #             a = 4;
    #             putIntLn(a);
    #         }
    #         a = 5;
    #         putIntLn(a);
    #     }
    #     """
    #     expect = """0\n1\n2\n3\n4\n5\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 538))

    # def test_block_stmt_local_var(self):
    #     input = """
    #     void main()
    #     {
    #         boolean a;
    #         a = true;
    #         putBoolLn(a);
    #         {
    #             int a;
    #             a = 1;
    #             putIntLn(a);
    #             {
    #                 int a;
    #                 a = -1;
    #                 putIntLn(a);
    #             }
    #             {
    #                 float a;
    #                 a = -1;
    #                 putFloatLn(a);
    #             }
    #         }
    #     }
    #     """
    #     expect = """true\n1\n-1\n-1.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 540))

    # def test_value_complex_exp_No4(self):
    #     input = """
    #     int a[4];
    #     int foo(int a)
    #     {
    #         return a + 1;
    #     }
    #     void main()
    #     {
    #         a[2] = 80/8+9;
    #         putInt(foo(a[2])+1);
    #     }
    #     """
    #     expect = """21"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 541))

    # def test_value_complex_exp_No5(self):
    #     input = """
    #     float func(float x) 
    #     { 
    #         return x*x*x - x*x + 2; 
    #     } 
    #     float derivFunc(float x) 
    #     { 
    #         return 3*x*x - 2*x; 
    #     }  
    #     void main() 
    #     { 
    #         float x0; x0= -20; 
    #         putFloatLn(func(x0));
    #         putFloatLn(derivFunc(x0));

    #     } 
    #     """
    #     expect = """-8398.0\n1240.0\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 542))

    # def test_value_complex_exp_No6(self):
    #     input = """
    #      int c()
    #         {
    #             return 1;
    #         }
    #     void main(){
    #             int arr[5]; 
    #             arr[0] = 5; 
    #             arr[2] = -10; 
    #             arr[3 / 2] = 2; 
    #             arr[3] = arr[0]; 
    #             putInt(arr[0]);
    #             putInt(arr[1]);
    #             putInt(arr[2]);
    #             putInt(arr[3]);
    #             putInt(c()+3); 
    #        }
    #     """
    #     expect = """52-1054"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 543))

    # def test_value_complex_exp_No7(self):
    #     input = """
    #     void main(){
    #         boolean A,B,C,D,E,F,G;
    #         A = true;
    #         B= false;
    #         C = false;
    #         D = true;
    #         E = false;
    #         F = true;
    #         G = false;
    #         putBoolLn(A&&!B&&C||A&&!B&&!C == A&&!B);
    #         putBoolLn(A&&B&&C||A&&B&&D||A&&B == A&&B);
    #         putBoolLn(!(!A||!(B&&C))&&!A == false);
    #         putBoolLn(A&&(!A||B) == A&&B);
    #         putBoolLn((A||B)&&(A||!B)== A);
    #         putBoolLn(A || B&&C == (A||B)&&(A||C));
    #         putBoolLn(!A&&!B || !A&&C || B&&!C || A&&!B&&!C == !(A&&C));
    #         putBoolLn(!A&&!B&&C || !A&&B&&!C || A&&!(B&&C));
    #         putBoolLn(!(!(!A&&!B&&C)&&!(!A&&B&&!C)&&!(A&&!(B&&C))));
    #         return;
    #     }
    #     """
    #     expect = """true\nfalse\nfalse\nfalse\ntrue\ntrue\ntrue\ntrue\ntrue\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 544))

    # def test_value_complex_exp_No8(self):
    #     input = """
    #     int a[3];
    #     void main(){
    #         int b[3];
    #         float c;
    #         b[0] = 1;
    #         b[2] = a[2];
    #         a[1] = 2;
    #         a[0] = b[2];
    #         c = a[2];
    #         putFloatLn(0.0);
    #         putString("Success");
    #     }
    #     """
    #     expect = """0.0\nSuccess"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 545))

    # def test_if_stmt_value_in_thenStmt(self):
    #     input = """
    #     int a;
    #     void main(){
    #         if (a==0)
    #             putIntLn(2);
    #     }
    #     """
    #     expect = """2\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 546))

    # def test_if_stmt_value_in_elseStmt(self):
    #     input = """
    #     int a;
    #     void main(){
    #         if (a==1)
    #             putIntLn(2);
    #         else
    #             putIntLn(1);
    #     }
    #     """
    #     expect = """1\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 547))

    # def test_if_stmt_call_exp_in_exp_if(self):
    #     input = """
    #     boolean gT(int a, int b)
    #     {
    #         return a > b;
    #     }
    #     void main(){
    #         int a, b;
    #         a = 1;
    #         b = 2;
    #         if (false && gT(a,b))
    #             putIntLn(2);
    #         else
    #             putIntLn(1);
    #     }
    #     """
    #     expect = """1\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 548))

    # def test_if_stmt_shortcut_and_op_No1(self):
    #     input = """
    #     int a;
    #     void main(){
    #         if (false && a/0 > 0)
    #             putString("Sai roi");
    #         else
    #             putString("Success");
    #     }
    #     """
    #     expect = """Success"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 549))

    # def test_if_stmt_shortcut_and_op_No2(self):
    #     input = """
    #     boolean gT(int a, int b) 
    #     { return a > b;}
    #     boolean lT(int a, int b) 
    #     { return a < b;}
    #     void main(){
    #         int a ; a = 1;
    #         int b ; b = 2;
    #         if (lT(a,b) && gT(b,a))
    #             putString("1");
    #         if (lT(a,b) && gT(a,b))
    #             putString("2");
    #     }
    #     """
    #     expect = """1"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 550))

    # def test_if_stmt_shortcut_or_op_No1(self):
    #     input = """
    #     int a;
    #     void main(){
    #         if (true || a/0)
    #             putString("Sai roi");
    #         else
    #             putString("Success");
    #     }
    #     """
    #     expect = """Sai roi"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 551))

    # def test_if_stmt_shortcut_or_op_No2(self):
    #     input = """
    #     boolean gT(int a, int b) 
    #     { return a > b;}
    #     boolean lT(int a, int b) 
    #     { return a < b;}
    #     void main(){
    #         int a ; a = 1;
    #         int b ; b = 2;
    #         if (lT(a,b) || gT(b,a))
    #             putString("1");
    #         if (gT(a,b) || gT(a,b))
    #             putString("2");
    #     }
    #     """
    #     expect = """1"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 552))

    # def test_if_stmt_in_recur_No1(self):
    #     input = """
    #     int sum(int a, int b)
    #     {
    #         if (a>b) 
    #             return 0;
    #         return a+sum(a+1,b);
    #     }
    #     void main(){
    #         int max, min;
    #         max =10;
    #         min = 1;
    #         putInt(sum(min,max));
    #     }
    #     """
    #     expect = """55"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 553))

    # def test_if_stmt_in_recur_No2(self):
    #     input = """
    #      int giai_thua(int n){
    #         if (n<=1) 
    #             return 1;
    #         else
    #             return n*giai_thua(n-1);
    #     }
    #     void main() {
    #         int a;
    #         a=6;
    #         putInt(giai_thua(a));
    #     }
    #     """
    #     expect = """720"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 554))

    # def test_for_stmt_No1(self):
    #     input = """
    #     void main() {
    #         int i;
    #         for(i=1;i<10;i=i+1)
    #             putInt(i);
    #     }
    #     """
    #     expect = """123456789"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 555))

    # def test_for_stmt_No2(self):
    #     input = """
    #     void main() {
    #         int i;
    #         i = 1;
    #         for(i;i<10;i=i+1)
    #             putInt(i);
    #     }
    #     """
    #     expect = """123456789"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 556))

    # def test_for_stmt_No3(self):
    #     input = """
    #     void main() {
    #         int i;
    #         i = 1;
    #         for(i;false;i=i+1)
    #             putInt(i);
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 557))

    # def test_for_stmt_No4(self):
    #     input = """
    #     void main() {
    #         int i;
    #         i = 10;
    #         for(i;i>1;i=i-1)
    #             putInt(i);
    #     }
    #     """
    #     expect = """1098765432"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 558))

    # def test_for_stmt_No5(self):
    #     input = """
    #     void main() {
    #         int i;
    #         i = 10;
    #         for(i;i>1;i)
    #         {
    #             putInt(i);
    #             i=i-1;
    #         }
    #     }
    #     """
    #     expect = """1098765432"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 559))

    # def test_for_stmt_w_brk_stmt(self):
    #     input = """
    #     void main() {
    #         int i;
    #         for(i=1;i<10;i=i+1)
    #         {
    #             if (i==6)
    #             break;
    #             else 
    #                 putInt(i);
    #         }
    #     }
    #     """
    #     expect = """12345"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 560))

    # def test_for_stmt_w_conti_stmt(self):
    #     input = """
    #     void main() {
    #         int i;
    #         for(i=1;i<10;i=i+1)
    #         {
    #             if (i%2==0) continue;
    #             else putInt(i);
    #         }
    #     }
    #     """
    #     expect = """13579"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 561))

    # def test_for_stmt_w_conti_and_brk_stmt(self):
    #     input = """
    #     void main() {
    #         int i;
    #         for(i=1;i<10;i=i+1)
    #         {
    #             if (i%2==0) continue;
    #             else 
    #                 if (i==7) break; 
    #                 else putInt(i);
    #         }
    #     }
    #     """
    #     expect = """135"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 562))

    # def test_for_stmt_complex_No1(self):
    #     input = """
    #     void main() {
    #         int a,b;
    #         for(a=2;a<10;a=a+1)
    #         {
    #             for (b = 1;b<=10;b=b+1)
    #             {   
    #                 if (a*b<10)
    #                     putString(" ");
    #                 putInt(a*b);
    #                 putString(" ");                    
    #             }
    #             putLn();
    #         }
    #     }
    #     """
    #     expect = """ 2  4  6  8 10 12 14 16 18 20 \n 3  6  9 12 15 18 21 24 27 30 \n 4  8 12 16 20 24 28 32 36 40 \n 5 10 15 20 25 30 35 40 45 50 \n 6 12 18 24 30 36 42 48 54 60 \n 7 14 21 28 35 42 49 56 63 70 \n 8 16 24 32 40 48 56 64 72 80 \n 9 18 27 36 45 54 63 72 81 90 \n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 563))

    # def test_for_stmt_complex_No2(self):
    #     input = """
    #     void insertionSort(int arr[], int n) 
    #     { 
    #         int i, key, j; 
    #         for (i = 1; i < n; i=i+1) { 
    #             key = arr[i]; 
    #             for (j=i-1;j >= 0 && arr[j] > key;j=j-1) 
    #             {  
    #                 arr[j + 1] = arr[j];  
    #             }  
    #             arr[j + 1] = key; 
    #         } 
    #     } 
    #     void main()
    #     {
    #         int a[5],n;
    #         n = 5;
    #         a[0]=a[4]=1;
    #         a[1] = 2;
    #         a[2] =10;
    #         a[3] = -9;
    #         insertionSort(a,n);
    #         int i;
    #         for (i=0;i<n;i=i+1)
    #             putIntLn(a[i]);
    #     }
    #     """
    #     expect = """-9\n1\n1\n2\n10\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 564))

    # def test_for_stmt_complex_No3(self):
    #     input = """
    #     float Sin(float x){
    #         float t,sum;
    #         t = 1.0;
    #         sum = 0.0;
    #         int i,n;
    #         n = 1000;
    #         for(i=1;i<=n;i=i+1)
    #         {
    #             t=(-1)*t*x*x/(2*i*(2*i+1));
    #             sum=sum+t;
    #         }
    #         return sum;
    #     }
    #     void main()
    #     {
    #         putFloat(Sin(3.14));
    #     }
    #     """
    #     expect = """-0.9994928"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 565))

    # def test_while_stmt_No1(self):
    #     input = """
    #     void main()
    #     {
    #         int a;a = 3;
    #         do 
    #         {
    #             a = a + 3;
    #             putInt(a);
    #         }
    #         while (a<=10);
    #     }
    #     """
    #     expect = """6912"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 566))

    # def test_while_stmt_No2(self):
    #     input = """
    #     void main()
    #     {
    #         int i, sum;
    #         i = 0; sum = 0;
    #         do
    #             i=i+1;
    #             sum=sum+i;
    #         while (i<10);
    #         putInt(sum);
    #     }
    #     """
    #     expect = """55"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 567))

    # def test_while_stmt_No3(self):
    #     input = """
    #     boolean isPrime(int a)
    #     {
    #         if (a<=1) return false;
    #         int i; i = 1;
    #         do
    #             i=i+1;
    #         while(a % i !=0);
    #         if (i==a) return true;
    #         else 
    #             return false;
    #     }
    #     void main()
    #     {
    #         int i;
    #         i = 1;
    #         do
    #             i = i+1;
    #             if (isPrime(i))
    #                 putInt(i);
    #         while (i<20);
    #     }
    #     """
    #     expect = """235711131719"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 568))

    # def test_while_stmt_w_brk(self):
    #     input = """
    #     void main()
    #     {
    #         int i;
    #         int sum;
    #         sum = 0;
    #         i = 1;
    #         do 
    #             i=i+1;sum=sum-1;
    #             if (i > 10) break;
    #         while(true);
    #         putInt(sum);
    #     }
    #     """
    #     expect = """-10"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 569))

    # def test_while_stmt_w_conti(self):
    #     input = """
    #     void main()
    #     {
    #         int i;
    #         i = 0;
    #         do 
    #             i = i+ 1;
    #             if (i%2==0||i%3 == 0) continue;
    #             putInt(i);
    #         while (i<10);
    #     }
    #     """
    #     expect = """157"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 570))

    # def test_while_stmt_w_conti_and_brk(self):
    #     input = """
    #     void main()
    #     {
    #         int i;
    #         i = 0;
    #         do 
    #             i = i+ 1;
    #             if (i%2==0||i%3 == 0) continue;
    #             else if (i>20) break;
    #             putInt(i);
    #         while (true);
    #     }
    #     """
    #     expect = """15711131719"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 571))

    # def test_return_stmt_in_int_type(self):
    #     input = """
    #     int foo(int a)
    #     {
    #         return a*3;
    #     }
    #     void main()
    #     {
    #         int a; a=4;
    #         putInt(foo(a));
    #     }
    #     """
    #     expect = """12"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 572))

    # def test_return_stmt_in_float_type(self):
    #     input = """
    #     float foo(int a)
    #     {
    #         return a*3;
    #     }
    #     void main()
    #     {
    #         int a; a=4;
    #         putFloat(foo(a));
    #     }
    #     """
    #     expect = """12.0"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 573))

    # def test_return_stmt_in_boolean_type_and_string_type(self):
    #     input = """
    #     boolean xor(boolean A, boolean B)
    #     {
    #         return (A&&!B)||(B&&!A);
    #     }
    #     void main()
    #     {
    #         putString("F xor F = "); putBoolLn(xor(false,false));
    #         putString("F xor T = "); putBoolLn(xor(false,true));
    #         putString("T xor F = "); putBoolLn(xor(true,false));
    #         putString("T xor T = "); putBoolLn(xor(true,true));
    #     }
    #     """
    #     expect = """F xor F = false\nF xor T = true\nT xor F = true\nT xor T = false\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 574))

    # def test_return_stmt_in_array_pointer_type(self):
    #     input = """
    #     int[] foo()
    #     {
    #         int a[4];
    #         a[0] = 9; a[2]= 2; a[1]=4;
    #         return a;
    #     }
    #     void main()
    #     {
    #        putInt(foo()[2] + foo()[0]);
    #     }
    #     """
    #     expect = """11"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 575))

    # def test_use_var_glo_vs_var_loc(self):
    #     input = """
    #     int a;
    #     void main() {
    #         a = 1;
    #         {
    #             putInt(a);
    #             int a;
    #             a = 2;
    #             putInt(a);
    #         }
    #         putInt(a);
    #     }
    #     """
    #     expect = """121"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 576))

    # def test_bubblesort(self):
    #     input = """
    #     void main() {
    #         int a[5];
    #         int i;
    #         for (i=0;i<5;i=i+1){
    #             a[i] = 5-i;
    #         }
    #         int j;
    #         for (j=0;j<5;j = j+1){
    #             for (i=0;i<4;i=i+1){
    #                 if (a[i] > a[i+1]){
    #                     int tmp;
    #                     tmp = a[i];
    #                     a[i] = a[i+1];
    #                     a[i+1] = tmp;
    #                 }
    #             }
    #         }
    #         for (i=0;i<5;i=i+1){
    #             putInt(a[i]);
    #         }
    #     }
    #     """
    #     expect = """12345"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 577))

    # def test_fibo_recur(self):
    #     input = """
    #     int fibo(int n) {
    #         if (n == 1) return 1;
    #         if (n == 0) return 0;
    #         return fibo(n-1) + fibo(n-2);
    #     }
    #     void main() {
    #         putInt(fibo(5));
    #     }
    #     """
    #     expect = """5"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 578))

    # def test_print_str(self):
    #     input = """
    #     string helo() {
    #         string a;
    #         a = "helo bac si";
    #         return a;
    #     }
    #     void main() {
    #         putString(helo());
    #     }
    #     """
    #     expect = """helo bac si"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 579))

    # def test_dowhile_assign_var(self):
    #     input = """
    #     void main() {
    #         int a,b;
    #         a = b = 2;
    #         a + b;
    #         do {
    #             int a;
    #             a = 3;
    #         } while (a - b != 0);
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 580))

    # def test_mix_up_assign_op(self):
    #     input = """
    #     void main() {
    #         int a;
    #         float b;
    #         b = a = 2;
    #         putFloat(b);
    #     }
    #     """
    #     expect = """2.0"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 581))

    # def test_assign_in_exp(self):
    #     input = """
    #     void main() {
    #         int a;
    #         float b;
    #         a = 1;
    #         2 + (b = a = 2);
    #         putInt(a);
    #     }
    #     """
    #     expect = """2"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 582))

    # def test_assign_in_exp_w_shortcut(self):
    #     input = """
    #     void main() {
    #         int a, c;
    #         float b;
    #         a = 1;
    #         true || a + (b = a = 2) > 0;
    #         putInt(a);
    #     }
    #     """
    #     expect = """1"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 583))

    # def test_much_array(self):
    #     input = """
    #     int a[5];
    #     string b[5];
    #     float c[5];
    #     boolean d[5];
    #     void main() {
    #         int a[5];
    #         string b[5];
    #         float c[5];
    #         boolean d[5];
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 584))

    # def test_assign_intcell_to_float_cell(self):
    #     input = """
    #     int a[5];
    #     string b[5];
    #     float c[5];
    #     boolean d[5];
    #     void main() {
    #         a[1] = 2;
    #         c[1] = a[1];
    #         putFloat(c[1]);
    #     }
    #     """
    #     expect = """2.0"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 585))

    # def test_print_assign_param(self):
    #     input = """
    #     int a[5];
    #     string b[5];
    #     float c[5];
    #     boolean d[5];
    #     void main() {
    #         putFloat(c[1] = 3);
    #     }
    #     """
    #     expect = """3.0"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 586))

    # def test_assign_unop(self):
    #     input = """
    #     int a[5];
    #     string b[5];
    #     float c[5];
    #     boolean d[5];
    #     void main() {
    #         -(c[1] = 3);
    #         putFloat(c[1]);
    #     }
    #     """
    #     expect = """3.0"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 587))

    # def test_assign_bitop(self):
    #     input = """
    #     int a[5];
    #     string b[5];
    #     float c[5];
    #     boolean d[5];
    #     void main() {
    #         (d[1] = true) && false;
    #         putBool(d[1]);
    #     }
    #     """
    #     expect = """true"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 588))

    # def test_assign_w_reop(self):
    #     input = """
    #     int a[5];
    #     string b[5];
    #     float c[5];
    #     boolean d[5];
    #     void main() {
    #         (a[1] = 2) > 2;
    #         putInt(a[1]);
    #     }
    #     """
    #     expect = """2"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 589))

    # def test_program_w_print(self):
    #     input = """
    #     void print(int a) {
    #         putInt(a);
    #     }
    #     void main() {
    #         print(1);
    #     }
    #     """
    #     expect = """1"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 590))

    # def test_pro_w_add(self):
    #     input = """
    #     void print(int a) {
    #         putInt(a);
    #     }
    #     int add(int a, int b) {
    #         return a + b;
    #     }
    #     void main() {
    #         print(add(159, 753));
    #     }
    #     """
    #     expect = """912"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 591))

    # def test_pro_w_div(self):
    #     input = """
    #     void print(int a) {
    #         putInt(a);
    #     }
    #     int add(int a, int b) {
    #         return a + b;
    #     }
    #     int div(int a, int b) {
    #         return a/b;
    #     }
    #     void main() {
    #         print(div(add(159, 753),2));
    #     }
    #     """
    #     expect = """456"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 592))

    # def test_pro_w_mod(self):
    #     input = """
    #     void print(int a) {
    #         putInt(a);
    #     }
    #     int add(int a, int b) {
    #         return a + b;
    #     }
    #     int div(int a, int b) {
    #         return a/b;
    #     }
    #     int mod(int a, int b) {
    #         return a%b;
    #     }
    #     void main() {
    #         print(mod(div(add(159, 753),2),2));
    #     }
    #     """
    #     expect = """0"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 593))

    # def test_pro_check_prime(self):
    #     input = """
    #     boolean isPrim(int a) {
    #         if (a <= 1) return false;
    #         int i;
    #         for (i = 2; i < a/2+1; i=i+1) {
    #             if (a%i==0) return false;
    #         }
    #         return true;
    #     }
    #     void main() {
    #         putBool(isPrim(137));
    #     }
    #     """
    #     expect = """true"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 594))

    # def test_pro_check_gcd(self):
    #     input = """
    #     int gcd(int a, int b) {
    #         if (b == 0) return a;
    #         return gcd(b, a%b);
    #     }
    #     void main() {
    #         putInt(gcd(6,10));
    #     }
    #     """
    #     expect = """2"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 595))

    # def test_pro_check_lcm(self):
    #     input = """
    #     int lcm(int a, int b) {
    #         return a*b/gcd(a,b);
    #     }
    #     int gcd(int a, int b) {
    #         if (b == 0) return a;
    #         return gcd(b, a%b);
    #     }
    #     void main() {
    #         putInt(lcm(6,10));
    #     }
    #     """
    #     expect = """30"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 596))

    # def test_pro_checksum(self):
    #     input = """
    #     int checksum(int a[]) {
    #         int sum, i;
    #         sum = 0;
    #         for (i = 0; i < 10; i = i + 1) {
    #             sum = sum + a[i];
    #         }
    #         return sum;
    #     }
    #     int a[10];
    #     void main() {
    #         a[1] = 1;
    #         a[2] = 2;
    #         putInt(checksum(a));
    #     }
    #     """
    #     expect = """3"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 597))

    # def test_pro_xor(self):
    #     input = """
    #     boolean xor(boolean a, boolean b) {
    #         return a != b;
    #     }
    #     void main() {
    #         putBool(xor(true, false));
    #     }
    #     """
    #     expect = """true"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 598))

    # def test_pro_feel_good(self):
    #     input = """
    #     boolean feel(int a) {
    #         if (a > 0) return true;
    #         return false;
    #     }
    #     boolean good(int a) {
    #         if (a*a-a+a/a%a == 0) return true;
    #         return false;
    #     }
    #     void main() {
    #         putBool(feel(0) || good(-1));
    #     }
    #     """
    #     expect = """false"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 599))

    # def test_value_complex_program_No1(self):
    #     input = """
    #     int f()
    #     {
    #         return 200;
    #     }
    #     void main(){
    #         int main;
    #         main = f();
    #         putIntLn(main);
    #         {
    #             int i;
    #             int main;
    #             int f;
    #             main = f = i = 100;
    #             putIntLn(i);
    #             putIntLn(main);
    #             putIntLn(f);
    #         }
    #         putIntLn(main);
    #     }
    #     """
    #     expect = """200\n100\n100\n100\n200\n"""
    #     self.assertTrue(TestCodeGen.test(input, expect, 600))