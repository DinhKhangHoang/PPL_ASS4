import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,501))
        
    def test_02(self):
        input = """int b[9];
        float c;
        void main() {
            int d[10];
            putInt(100);
            float e;
            putFloat(5.2);
        }
        """
        expect = "1005.2"
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test_03(self):
        input = """int b[9];
        float c;
        void main() {
            int d[10];
            putInt(100);
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_04(self):
        input = """int b[9];
        float c;
        void main() {
            int d[10];
            putInt(100);
            {
                7;
                int e[5];
                8;
            }
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_05(self):
        input = """int b[9];
        float c;
        void main() {
            int d[10];
            if(true){
                putInt(5);
            }
            else{
                putFloat(5.2);
            }
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_06(self):
        input = """int b[9];
        float c;
        void main() {
            int d[10];
            if(false){
                putInt(5);
            }
            else{
                putFloat(5.2);
            }
        }
        """
        expect = "5.2"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_07(self):
        input = """int b[9];
        float c;
        void main() {
            int d[10];
            if(false){
                putInt(5);
            }
            else{
                putFloat(5.2);
            }
        }
        """
        expect = "5.2"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_08(self):
        input = """int b[9];
        float c;
        void main() {
            if(false){
                c;
                putInt(5);
            }
            else{
                putFloat(5.2);
            }
            
        }
        """
        expect = "5.2"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_09(self):
        input = """int b[9];
        float c;
        void main() {
            boolean b;
            b = true;
            if(b){
                c;
                putInt(5);
            }
            else{
                putFloat(5.2);
            }
            
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_10(self):
        input = """int b[9];
        float c;
        void main() {
            boolean b, c;
            b = true;
            c = false;
            b = b || c;
            if(b){
                c;
                putInt(5);
            }
            else{
                putFloat(5.2);
            }
            
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_11(self):
        input = """int b[9];
        float c;
        void main() {
            boolean b, c;
            b = true;
            c = false;
            b = b && c;
            if(b){
                c;
                putInt(5);
            }
            else{
                putFloat(5.2);
            }
            
        }
        """
        expect = "5.2"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_12(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_13(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            boolean e[2];
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_14(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            {
                boolean e[2];
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_vardecl_in_many_scope(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            {
                boolean e[2];
                {
                    int a[5];
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_vardecl_in_many_scope2(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            {
                boolean e[2];
                {
                    int a[5];
                }
                {
                    string f[2];
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_gencode_for_if(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            if(true){
                if(false)
                   putIntLn(34);
            }
            else{
                putInt(5);
            }
            putFloat(7.8);
        }
        """
        expect = "7.8"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_gencode_for_if2(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            if(true){
                if(false)
                   putIntLn(34);
                else{
                    putFloatLn(5.6);
                }
            }
            else{
                putInt(5);
            }
            putFloat(7.8);
        }
        """
        expect = """5.6
7.8"""
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_gencode_for_if3(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            if(true){
                if(false)
                   putIntLn(34);
                else{
                    if(true){
                        putString("khang goes pro");
                    }
                    else{
                        putString("khang cant go pro");
                    }
                }
            }
            else{
                putInt(5);
            }
            putFloat(7.8);
        }
        """
        expect = "khang goes pro7.8"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_gencode_for_if4(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            if(true){
                if(false)
                   putIntLn(34);
                else{
                    if(true){
                        putString("khang goes pro");
                    }
                    else{
                        putString("khang cant go pro");
                    }
                }
            }
            else{
                putInt(5);
            }
            putFloat(7.8);
        }
        """
        expect = "khang goes pro7.8"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_gencode_for_if5(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            if(false){
                if(false)
                   putIntLn(34);
                else{
                    if(true){
                        putString("khang goes pro");
                    }
                    else{
                        putString("khang cant go pro");
                    }
                }
            }
            else{
                putInt(5);
                if(true)
                    putFloat(8.9);
                if(false){
                    putInt(10);
                }
                else{
                    putFloat(1011);
                }
            }
            putFloat(7.8);
        }
        """
        expect = "58.91011.07.8"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_gencode_for_if6(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            if(false){
                if(false)
                   putIntLn(34);
                else{
                    if(true){
                        putString("khang goes pro");
                    }
                    else{
                        putString("khang cant go pro");
                    }
                }
            }
            else{
                putInt(5);
                if(true)
                    putFloat(8.9);
                if(true){
                    if(false)
                        putInt(10);
                    else
                        putFloat(13);
                }
                else{
                    putFloat(1011);
                }
            }
            putFloat(7.8);
        }
        """
        expect = "58.913.07.8"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_gencode_for_forstmt(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            int i, a;
            a = 1;
            for(i = 1 ; i < 10; i = i + 1){
                a = a * i;
            }
            putInt(a);
        }
        """
        expect = "362880"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_gencode_for_forstmt1(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            int i, a;
            a = 1;
            for(i = 1 ; i < 10; i = i + 1){
                //a = a * i;
            }
            putInt(a);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_gencode_for_forstmt2(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            int i, j, a;
            a = 1;
            for(i = 0 ; i < 10; i = i + 1){
                for(j = 1 ; j < 10; j = j +1){
                    a = a + j;
                }
            }
            putInt(a);
        }
        """
        expect = "451"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_gencode_for_forstmt3(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            int i, j, a;
            a = 1;
            for(i = 1 ; i < 10; i = i + 1){
                for(j = 1 ; j < 10; j = j +1){
                    a = a + j;
                }
                for(j = 1; j < 10; j = j + 1)
                    a = a + j;
            }
            putInt(a);
        }
        """
        expect = "811"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_gencode_for_forstmt4(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            int i, j, a;
            a = 1;
            for(i = 1 ; i < 10; i = i + 1){
                for(j = 1 ; j < 10; j = j +1){
                    a = a + j;
                }
            }
            for(j = 1; j < 10; j = j + 1)
                a = a + j;
            putInt(a);
        }
        """
        expect = "451"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_gencode_for_forstmt5(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            int i, j, a;
            a = 1;
            for(i = 1 ; i < 10; i = i + 1){
                for(j = 1 ; j < 10; j = j +1){
                    a = a + j;
                }
            }
            for(i = 1 ; i < 10; i = i + 1){
                for(j = 1 ; j < 10; j = j +1){
                    a = a + j;
                }
            }
            putInt(a);
        }
        """
        expect = "811"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_gencode_for_forstmt6(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            int i, j, a;
            a = 1;
            for(i = 1 ; i < 10; i = i + 1){
                for(j = 1 ; j < 10; j = j +1){
                    a = a + j;
                }
            }
            for(i = 1 ; i < 10; i = i + 1){
                for(j = 1 ; j < 10; j = j +1){
                    a = a + j;
                }
            }
            putInt(a);
        }
        """
        expect = "811"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_gencode_for_dowhilestmt(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            int i, j, a;
            a = 1;
            i = 0;
            do{
                a = a + i;
                i = i + 1;
            }while(i <= 10);
            putInt(a);
        }
        """
        expect = "56"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_gencode_for_dowhilestmt1(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            int i, j, a;
            a = 1;
            i = 0;
            do{
                a = a + i;
                i = i + 1;
            }while(i <= 10);
            do{
                a = a + i;
                i = i + 1;
            }while(i <= 10);
            putInt(a);
        }
        """
        expect = "67"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_gencode_for_dowhilestmt2(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            int i, j, a;
            a = 1;
            i = 0;
            do{
                a = a + i;
                i = i + 1;
                j = 0;
                do{
                    a = a + i;
                    j = j + 1;
                }while(j <= 10);
            }while(i <= 10);
            
            putInt(a);
        }
        """
        expect = "782"
        self.assertTrue(TestCodeGen.test(input,expect,532))

    def test_gencode_for_dowhilestmt3(self):
        input = """int b[9];
        float c;
        float d[10];
        void main() {
            int i, j, a;
            a = 1;
            i = 0;
            do{
                a = a + i;
                i = i + 1;
                j = 0;
                do{
                    int k;
                    k = 0;
                   do{
                       a = a + 1;
                       k = k + 1;
                   }while(k <= 10);
                    j = j + 1;
                }while(j <= 10);
            }while(i <= 10);
            
            putInt(a);
        }
        """
        expect = "1387"
        self.assertTrue(TestCodeGen.test(input,expect,533))

    def test_gencode_for_dowhilestmt4(self):
        input = """int a, b;
        void main(){
            a = 0;
            b = 8;
            float f;
            f = 7.8;
            do{
                do{
                    f = f + 1;
                }while(f < 10);
            }while(false);
            putFloat(f);
        }
        """
        expect = "10.8"
        self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_gencode_for_dowhilestmt5(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 0;
            do{
                c[i] = i;
                i = i + 1;
            }while(i < 10);
            putInt(c[7]);
        }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_gencode_for_for35(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 0;
            for(i = 0; i < 10; i = i + 1)
                c[i] = i*i;
            putInt(c[7]);
        }
        """
        expect = "49"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_gencode_for_dowhile7(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            do{
                c[i] = i;
                i = i - 1;
            }while(i >= 0);
            putInt(c[5]);
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_gencode_for_dowhile8(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            do{
                c[i] = i*i;
                i = i - 1;
            }while(i >= 0);
            putInt(c[5] + c[6] + c[7]);
        }
        """
        expect = "110"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_gencode_for_break(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            do{
                c[i] = i*i;
                i = i - 1;
                break;
            }while(i >= 0);
            putInt(i);
        }
        """
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_gencode_for_break1(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            do{
                i = i - 1;
                if (i < 5)
                    break;
            }while(i >= 0);
            putInt(i);
        }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    
    def test_gencode_for_break2(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            do{
                do{
                    i = i -1;
                }while(i > 5);
                break;
            }while(i >= 0);
            putInt(i);
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,541))
    
    def test_gencode_for_break3(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            do{
                do{
                    i = i -1;
                    if(true)
                        break;
                }while(i > 5);
                i = i -1;
            }while(i >= 0);
            putInt(i);
        }
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    
    def test_gencode_for_break4(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            do{
                do{
                    i = i -1;
                    if(true)
                        break;
                }while(i > 5);
                do{
                    i = i -1;
                    if(true)
                        break;
                }while(i > 5);
            }while(i >= -1);
            putInt(i);
        }
        """
        expect = "-3"
        self.assertTrue(TestCodeGen.test(input,expect,543))
    
    def test_gencode_for_break5(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            do{
                do{
                    do{
                        i = i -1;
                        if(true)
                            break;
                    }while(i > 5);
                    i = i -1;
                    if(true)
                        break;
                }while(i > 5);
                i = i -1;
            }while(i >= 0);
            putInt(i);
        }
        """
        expect = "-3"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    
    def test_gencode_for_break6(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            do{
                do{
                    do{
                        i = i -1;
                        if(true)
                            break;
                    }while(i > 5);
                    i = i -1;
                    if(true)
                        break;
                }while(i > 5);
                do{
                    i = i -1;
                    if (true)
                        break;
                }while(i > 5);
                i = i -1;
            }while(i >= 0);
            putInt(i);
        }
        """
        expect = "-3"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    
    def test_gencode_for_continue(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            for(i = 0; i < 10; i = i + 1){
                c[i] = 10 - i;
                if(true)
                    continue;
            }
            putInt(i);
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    
    def test_gencode_for_continue1(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            for(i = 0; i < 10; i = i + 1){
                c[i] = 10 - i;
                if(i < 5){
                    c[i] = c[i] * 2;
                    continue;
                }
                continue;
            }
            putInt(i);
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    
    def test_gencode_for_continue2(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            for(i = 0; i < 10; i = i + 1){
                c[i] = 10 - i;
                if(i < 5){
                    continue;
                }
                c[i] = c[i] * 3;
            }
            putInt(c[9]);
        }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,548))
    
    def test_gencode_for_continue3(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            for(i = 0; i < 10; i = i + 1){
                c[i] = 10 - i;
                int j;
                for(j = 0; j < 10; j = j + 1){
                    if(j < 5){
                        continue;
                    }
                    c[j] = c[j] * 4;
                }
                
            }
            putInt(c[9]);
        }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,549))
    
    def test_gencode_for_continue50(self):
        input = """int a, b;
        void main(){
            int c[10];
            int i;
            i = 9;
            for(i = 0; i < 10; i = i + 1){
                c[i] = 10 - i;
                int j;
                for(j = 0; j < 10; j = j + 1){
                    if(j < 5){
                        continue;
                    }
                    c[j] = c[j] * 4;
                }
                
            }
            putInt(c[9]);
        }
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,550))
    
    def test_print_out_value_of_global_array_types_element(self):
        input = """
        float a[5];
        float print(float a[]){ putFloat(a[1]); return 1;}
        void main () {
            float b[2];
            a = b;
            b[1] = 10.22e12;
            a[1]=1;
            print(a);
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_print_with_value_of_local_var_has_same_name_with_global_var_array(self):
        input = """boolean a[10]; void main () {int b;boolean a; {int c; a=true; putBool(!a);}}"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_print_out_value_of_global_array_var_int_type(self):
        input = """
        int a[5];
        int put(int a){return a;}
        void main () {
            int i;
            int b[2];
            b[1]=1;
            b[1];
            put(b[1]);
            putInt(put(b[1]));
            for(i=0;i<2;i=i+1)
                b[i] = i;
            a[3] = put(b[1]);
            putInt(a[3]);
        }
        """
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_print_out_value_of_var_check_and_symbol(self):
        input = """
        void main () {
            boolean a;
            a=false;
            true&&false&&true&&(a=true);
            putBool(a);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_print_out_value_of_var_check_or_symbol(self):
        input = """
        int a[5];
        void main () {
            boolean a;
            a=false;
            true||false||true||(a=true);
            putBool(a);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_print_out_value_of_var_check_and_or_with_complex_case(self):
        input = """
        int a[5];
        void main () {
            boolean a;
            a=false;
            if(false||false&&true && 12<5325.2 || (a!=false) ||(a=true)) {}
            putBool(a);
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_pass_arr_to_func(self):
        input = """
            void foo(int a[]) {
                putInt(a[0]);
            }
            void main() {
                int a[4];
                a[0] = 99;
                foo(a);
            }
        """
        expect = "99"
        self.assertTrue(TestCodeGen.test(input, expect, 557))
    
    def test_bool_array(self):
        input = """
            void main() {
                boolean a[3];
                a[0] = true;
                putBool(a[0]);
                putBool(12);
            }
        """
        expect = "truetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 558))
    
    def test_continue(self):
        input = """
            void main() {
                int i;
                i = 0;
                for (i = 0; i < 10; i = i + 1) {
                    if (i % 2 == 0) continue;
                    putInt(i);  
                }
            }
        """
        expect = "13579"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_var_decl(self):
        input = """
            boolean a[10];
            void main() {
                a[0] = true;
                a[1] = a[0] || (a[2] && a[3]);
                putBool(a[1]);
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 560))
    
    def test_var_decl_local(self):
        input = """
            void main() {
                boolean a[4];
                a[2] = a[3] = false;
                a[0] = true;
                a[1] = a[0] || (a[2] && a[3]);
                putBool(a[1]);
            }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 561))
    
    def test_pass_string_2_function(self):
        input = """
            float foo_1() {
                return 1;
            }
            void foo(string s, string arr[]) {
                putString(s);
                putString(arr[0]);
            } 
            void main() {
                string arr[1];
                arr[0] = "Hello";
                foo(arr[0], arr);
            }
        """
        expect = "HelloHello"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_pass_string_2_function_2(self):
        input = """
            int foo_1() {
                return 1;
            }
            void foo(boolean s, boolean arr[]) {
                putBool(s);
                putBool(arr[0]);
            } 
            void main() {
                boolean arr[1];
                arr[0] = false;
                foo(arr[0], arr);
            }
        """
        expect = "falsefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_pass_array_to_func(self):
        input = """
            void init_array(int arr[],int size) {
                int i;
                for (i = 0; i < size; i = i + 1) {
                    arr[i] = 3;
                }
            }
            void main() {
                int a[10];
                init_array(a, 10);
                putInt(a[3]);
            }
            int foo() {
                putInt(12);
            }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 564))
    
    def test_recursive_function(self):
        input = """
            int foo(int v) {
                if (v <= 1) return v;
                return foo(v-1) + foo(v-2);
            }
            void main() {
                putInt(foo(5));
            }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 565))
    
    def test_float_int_multiple(self):
        input = """
            void main() {
                putFloat(1.25*3);
            }
        """
        expect = "3.75"
        self.assertTrue(TestCodeGen.test(input, expect, 566))
    
    def test_for_complex_6(self):
        input = """
            int a; 
            float b;
            boolean c;
            int d[5];
            string s;
            void main()
            {
                int sum,i,j;
                sum = 20;
                for (i=1;i<=sum;i=i+1)
                    sum = sum -i;
                putInt(sum);        
            }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,567))
    def test_for_complex_7(self):
        input = """
            int a; 
            float b;
            boolean c;
            int d[5];
            string s;
            void main()
            {
                int sum,i,j;
                sum = 20;
                for (i=1;i<=sum;i=i+1)
                    i=i+1;
                putInt(i);   
            }
        """
        expect = "21"
        self.assertTrue(TestCodeGen.test(input,expect,568))
    
    def test_for_continue_break(self):
        input = """
        void main() {
            int i;
            for(i=1;i<10;i=i+1)
            {
                if (i%2==0) continue;
                if (i == 7) break;
                putInt(i);
            }
        }
        """
        expect = """135"""
        self.assertTrue(TestCodeGen.test(input,expect, 569))
    
    def test_return_in_nested_if(self):
        input = """
        int f(int value) {
            if (value > 2) {
                if (value > 2) {
                    return f(value - 1);
                } else {
                    return 1;
                }
            } else {
                return 1;
            }
        }
        void main() {
            putInt(1);
            f(3);
        }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input,expect, 570))
    
    def test_return_2_times(self):
        input = """
        int f(int value) {
            return value;
            return value;
        }
        void main() {
            putInt(f(1));
        }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input,expect, 571))
    
    def test_convert_int_to_float(self):
        input = """
        float foo(int a)
        {
            return a;
        }
        void main()
        {
            int a;
            a = 199;
            putFloat(foo(a));
        }
        """
        expect = """199.0"""
        self.assertTrue(TestCodeGen.test(input,expect,572))
    
    def test_void_return(self):
        input = """
        void main()
        {
            int a;
            a = 10;
            putInt(200);
            if (a==10) {return;}
            putInt(100);
        }
        """
        expect = """200"""
        self.assertTrue(TestCodeGen.test(input,expect,573))
    
    def test_value_of_complex_program_No6(self):
        input = """
        void max(int a[])
        {
            int max;
            if (1 < 2) max =a[0];
        }
        void main(){
            
            putInt(200);
        }
        """
        expect = '200'
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_use_var_glo_vs_var_loc(self):
        input = """
        int a;
        void main() {
            a = 1;
            {
                putInt(a);
                int a;
                a = 2;
                putInt(a);
            }
            putInt(a);
        }
        """
        expect = """121"""
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_return_array(self):
        input = """
        int[] foo()
        {
            int a[1];
            a[0] =100;
            return a;
        }
        void main()
        {
            putInt(foo()[0]);   
        }
        """
        expect = '100'
        self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_bubblesort(self):
        input = """
        void main() {
            int a[5];
            int i;
            for (i=0;i<5;i=i+1){
                a[i] = 5-i;
            }
            int j;
            for (j=0;j<5;j = j+1){
                for (i=0;i<4;i=i+1){
                    if (a[i] > a[i+1]){
                        int tmp;
                        tmp = a[i];
                        a[i] = a[i+1];
                        a[i+1] = tmp;
                    }
                }
            }
            for (i=0;i<5;i=i+1){
                putInt(a[i]);
            }
        }
        """
        expect = """12345"""
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_fibo_recur(self):
        input = """
        int fibo(int n) {
            if (n == 1) return 1;
            if (n == 0) return 0;
            return fibo(n-1) + fibo(n-2);
        }
        void main() {
            putInt(fibo(5));
        }
        """
        expect = """5"""
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_print_str(self):
        input = """
        string helo() {
            string a;
            a = "helo bac si";
            return a;
        }
        void main() {
            putString(helo());
        }
        """
        expect = """helo bac si"""
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_dowhile_assign_var(self):
        input = """
        void main() {
            int a,b;
            a = 2;
            b = 2;
            a + b;
            do {
                int a;
                a = 3;
            } while (a - b != 0);
        }
        """
        expect = """"""
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_mix_up_assign_op(self):
        input = """
        void main() {
            int a;
            float b;
            b = 2;
            putFloat(b);
        }
        """
        expect = """2.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_assign_in_exp(self):
        input = """
        void main() {
            int a;
            float b;
            a = 1;
            2 + (2);
            a = 2;
            putInt(a);
        }
        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_assign_in_exp_w_shortcut(self):
        input = """
        void main() {
            int a, c;
            float b;
            a = 1;
            true || a + (2) > 0;
            a = 2;
            b = 2;
            putInt(a);
        }
        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_much_array(self):
        input = """
        int a[5];
        string b[5];
        float c[5];
        boolean d[5];
        void main() {
            int a[5];
            string b[5];
            float c[5];
            boolean d[5];
        }
        """
        expect = """"""
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_assign_intcell_to_float_cell(self):
        input = """
        int a[5];
        string b[5];
        float c[5];
        boolean d[5];
        void main() {
            a[1] = 2;
            c[1] = a[1];
            putFloat(c[1]);
        }
        """
        expect = """2.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_print_assign_param(self):
        input = """
        int a[5];
        string b[5];
        float c[5];
        boolean d[5];
        void main() {
            putFloat(3);
        }
        """
        expect = """3.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_assign_unop(self):
        input = """
        int a[5];
        string b[5];
        float c[5];
        boolean d[5];
        void main() {
            c[1] = 3;
            putFloat(c[1]);
        }
        """
        expect = """3.0"""
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_assign_bitop(self):
        input = """
        int a[5];
        string b[5];
        float c[5];
        boolean d[5];
        void main() {
            d[1] = true;
            (d[1]) && false;
            putBool(d[1]);
        }
        """
        expect = """true"""
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_assign_w_reop(self):
        input = """
        int a[5];
        string b[5];
        float c[5];
        boolean d[5];
        void main() {
            a[1] = 2;
            (a[1]) > 2;
            putInt(a[1]);
        }
        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_program_w_print(self):
        input = """
        void print(int a) {
            putInt(a);
        }
        void main() {
            print(1);
        }
        """
        expect = """1"""
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_pro_w_add(self):
        input = """
        void print(int a) {
            putInt(a);
        }
        int add(int a, int b) {
            return a + b;
        }
        void main() {
            print(add(159, 753));
        }
        """
        expect = """912"""
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_pro_w_div(self):
        input = """
        void print(int a) {
            putInt(a);
        }
        int add(int a, int b) {
            return a + b;
        }
        int div(int a, int b) {
            return a/b;
        }
        void main() {
            print(div(add(159, 753),2));
        }
        """
        expect = """456"""
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_pro_w_mod(self):
        input = """
        void print(int a) {
            putInt(a);
        }
        int add(int a, int b) {
            return a + b;
        }
        int div(int a, int b) {
            return a/b;
        }
        int mod(int a, int b) {
            return a%b;
        }
        void main() {
            print(mod(div(add(159, 753),2),2));
        }
        """
        expect = """0"""
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_pro_check_prime(self):
        input = """
        boolean isPrim(int a) {
            if (a <= 1) return false;
            int i;
            for (i = 2; i < a/2+1; i=i+1) {
                if (a%i==0) return false;
            }
            return true;
        }
        void main() {
            putBool(isPrim(137));
        }
        """
        expect = """true"""
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_pro_check_gcd(self):
        input = """
        int gcd(int a, int b) {
            if (b == 0) return a;
            return gcd(b, a%b);
        }
        void main() {
            putInt(gcd(6,10));
        }
        """
        expect = """2"""
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_pro_check_lcm(self):
        input = """
        int lcm(int a, int b) {
            return a*b/gcd(a,b);
        }
        int gcd(int a, int b) {
            if (b == 0) return a;
            return gcd(b, a%b);
        }
        void main() {
            putInt(lcm(6,10));
        }
        """
        expect = """30"""
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_pro_checksum(self):
        input = """
        int checksum(int a[]) {
            int sum, i;
            sum = 0;
            for (i = 0; i < 10; i = i + 1) {
                sum = sum + a[i];
            }
            return sum;
        }
        int a[10];
        void main() {
            a[1] = 1;
            a[2] = 2;
            putInt(checksum(a));
        }
        """
        expect = """3"""
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_pro_xor(self):
        input = """
        boolean xor(boolean a, boolean b) {
            return a != b;
        }
        void main() {
            putBool(xor(true, false));
        }
        """
        expect = """true"""
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_pro_feel_good(self):
        input = """
        boolean feel(int a) {
            if (a > 0) return true;
            return false;
        }
        boolean good(int a) {
            if (a*a-a+a/a%a == 0) return true;
            return false;
        }
        void main() {
            putBool(feel(0) || good(-1));
        }
        """
        expect = """false"""
        self.assertTrue(TestCodeGen.test(input, expect, 599))

    def test_value_complex_program_No1(self):
        input = """
        int f()
        {
            return 200;
        }
        void main(){
            int main;
            main = f();
            putIntLn(main);
            {
                int i;
                int main;
                int f;
                main = 100;
                i = main;
                f = main;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            }
            putIntLn(main);
        }
        """
        expect = """200\n100\n100\n100\n200\n"""
        self.assertTrue(TestCodeGen.test(input, expect, 600))
