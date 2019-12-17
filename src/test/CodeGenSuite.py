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

    
