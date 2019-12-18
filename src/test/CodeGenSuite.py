import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    	expect = "5"
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
            }
            putInt(a);
        }
        """
        expect = "406"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    
