'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt",MType([],IntType()), CName(self.libName)),
                    Symbol("putIntLn",MType([IntType()],VoidType()), CName(self.libName)),
                    Symbol("putInt",MType([IntType()],VoidType()), CName(self.libName)),
                    Symbol("getFloat",MType([],FloatType()), CName(self.libName)),
                    Symbol("putFloat",MType([FloatType()],VoidType()), CName(self.libName)),
                    Symbol("putFloatLn",MType([FloatType()],VoidType()), CName(self.libName)),
                    Symbol("putBool",MType([BoolType()],VoidType()), CName(self.libName)),
                    Symbol("putBoolLn",MType([BoolType()],VoidType()), CName(self.libName)),
                    Symbol("putString",MType([StringType()],VoidType()), CName(self.libName)),
                    Symbol("putStringLn",MType([StringType()],VoidType()), CName(self.libName)),
                    Symbol("putLn",MType([],VoidType()), CName(self.libName))]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CParam():
    def __init__(self, sym, isGlobalArray, lstDeclArray):
        #sym: List[Symbol]
        #isGlobalArray: Boolean
        #lstDeclArray: List[VarDecl]

        self.sym = sym
        self.isGlobalArray = isGlobalArray
        self.lstDeclArray = lstDeclArray

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, [[]])
        lstArray = []
        for x in ast.decl:
            if type(x) is VarDecl:
                e = self.visit(x,e)
                #self.env = e.sym
                if type(x.varType) is ArrayType:
                    lstArray.append(x)
            else:
                e.sym[0].insert(0, Symbol(x.name.name, MType(list(map(lambda y: y.varType, x.param)) , x.returnType), CName(self.className)))
        e.sym[0] += self.env
        for x in ast.decl:
            if type(x) is FuncDecl:
                self.visit(x, SubBody(e.frame, [[]] + e.sym))

        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list())), CParam(c, False, []), Frame("<init>", VoidType))
        if len(lstArray) > 0:
            self.genMETHOD(FuncDecl(Id("<clinit>"), list(), None, Block([])), CParam(c, True, lstArray), Frame("<clinit>", VoidType))
        self.emit.emitEPILOG()
        return c

    def visitVarDecl(self, ast, o):
        #ast: VarDecl
        #o: SubBody
        #ast.variable: str
        #ast.varType: Type

        subctxt = o
        frame = subctxt.frame
        mtype = ast.varType
        name = ast.variable
        if frame is None:
            # Decl mot bien global
            self.emit.printout(self.emit.emitATTRIBUTE(name, mtype, False, ""))
            subctxt.sym[0].insert(0, Symbol(name, mtype, CName(self.className)))
            return SubBody(None, subctxt.sym)
        else:
            # Decl mot bien local hoac param
            idx = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, name, mtype, frame.getStartLabel(), frame.getEndLabel(), frame))
            subctxt.sym[0].insert(0, Symbol(name, mtype, Index(idx)))
            return SubBody(frame, subctxt.sym)
            

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: CParam
        #frame: Frame

        isGlobalArray = o.isGlobalArray
        lstDeclArray = o.lstDeclArray
        if isGlobalArray:
            # Constructor cho khai bao bien global la array
            returnType = VoidType()
            methodName = "<clinit>"
            intype = list()
            mtype = MType(intype, returnType)
            self.emit.printout(self.emit.emitMETHOD(methodName, mtype, True, frame))
            frame.enterScope(True)
            for x in lstDeclArray:
                lexeme = self.className + "." + x.variable
                #print(lexeme)
                #print(x.varType)
                self.emit.printout(self.emit.emitINITARRAY(lexeme, x.varType, frame))
            self.emit.printout(self.emit.emitRETURN(returnType, frame))
            self.emit.printout(self.emit.emitENDMETHOD(frame))
            # if frame.getStackSize() != 0:
            #     print(methodName)
            frame.exitScope()
        else:
            isInit = consdecl.returnType is None
            isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
            returnType = VoidType() if isInit else consdecl.returnType
            methodName = "<init>" if isInit else consdecl.name.name
            intype = [ArrayPointerType(StringType())] if isMain else list(map(lambda x: x.varType, consdecl.param))
            mtype = MType(intype, returnType)

            self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))  

            frame.enterScope(True)

            glenv = o.sym

            # Generate code for parameter declarations
            if isInit:
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
            elif isMain:
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            else:
                e = SubBody(frame, glenv)
                for x in consdecl.param:
                    e = self.visit(x, e)
                    glenv = e.sym
            self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

            # Generate code for statements
            if isInit:
                self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
                self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            #list(map(lambda x: self.visit(x, SubBody(frame, glenv)) if type(x) is not VarDecl else 1, body.member))
            body = consdecl.body
            if not isInit:
                e = SubBody(frame, glenv)
                for x in body.member:
                    if type(x) is VarDecl:
                        e = self.visit(x, e)
                        glenv = e.sym
                        if type(x.varType) is ArrayType:
                            idx = glenv[0][0].value.value
                            self.emit.printout(self.emit.emitINITARRAY(idx, x.varType, frame))
                    elif isinstance(x, Expr):
                        str1, typ1 = self.visit(x, Access(frame, glenv, False, True))
                        self.emit.printout(str1)
                        #print(frame.getStackSize())
                        if frame.getStackSize() > 0:
                            self.emit.printout(self.emit.emitPOP(frame))
                    elif isinstance(x, Block):
                        self.visit(x, SubBody(e.frame, [[]] + e.sym))
                    else:
                        self.visit(x, e)


            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
            self.emit.printout(self.emit.emitRETURN(returnType, frame))
            self.emit.printout(self.emit.emitENDMETHOD(frame))
            frame.exitScope()

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: SubBody(frame :Frame, sym: list(symbol)) = SubBody(None, envi)
        #name: Id
        #param: List[VarDecl]
        #returnType: Type
        #body: Block

        subctxt = o
        frame = Frame(ast.name.name, ast.returnType)
        self.genMETHOD(ast, CParam(subctxt.sym, False, list()), frame)
        #return SubBody(None, [Symbol(ast.name.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)
        return SubBody(None, subctxt.sym)

    def visitBlock(self, ast, o):
        #Block.member: list(BlockMember)
        ctxt = o
        frame = ctxt.frame
        glenv = ctxt.sym
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        e = SubBody(frame, glenv)
        #print(frame.getStackSize())
        for x in ast.member:
            if isinstance(x, Block):
                self.visit(x, SubBody(e.frame, [[]] + e.sym))
            elif isinstance(x, Decl):
                e = self.visit(x, e)
                glenv = e.sym
                if type(x.varType) is ArrayType:
                    idx = glenv[0][0].value.value
                    self.emit.printout(self.emit.emitINITARRAY(idx, x.varType, e.frame))
            elif isinstance(x, Expr) is False:
                self.visit(x, e)
            else:
                str1, typ1 = self.visit(x, Access(e.frame, glenv, False, True))
                self.emit.printout(str1)
                #print(frame.getStackSize())
                if frame.getStackSize() > 0:
                    self.emit.printout(self.emit.emitPOP(frame))
                #if isinstance(x, LHS):
                #    self.emit.printout(self.emit.emitPOP(frame))
                
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()
            
    def visitDowhile(self, ast, o):
        #sl:List[Stmt]
        #exp: Expr
        ctxt = o
        frame = ctxt.frame
        glenv = ctxt.sym
        frame.enterLoop()
        labelContinue = frame.getContinueLabel()
        labelBreak = frame.getBreakLabel()
        label_first = frame.getNewLabel()
        self.emit.printout(self.emit.emitLABEL(label_first, frame))
        e = SubBody(frame, glenv)
        for x in ast.sl:
            if isinstance(x, Expr):
                str1, typ1 = self.visit(x, Access(frame, glenv, False, True))
                self.emit.printout(str1)
                if frame.getStackSize() > 0:
                    self.emit.printout(self.emit.emitPOP(frame))
                #if isinstance(x, LHS):
                #    self.emit.printout(self.emit.emitPOP(frame))
            elif type(x) is Block:
                self.visit(x, SubBody(e.frame, [[]] + e.sym))
            elif isinstance(x, Stmt):
                self.visit(x, e)
        self.emit.printout(self.emit.emitLABEL(labelContinue, frame))
        str1, typ1 = self.visit(ast.expr, Access(frame, glenv, False, True))
        self.emit.printout(str1)
        self.emit.printout(self.emit.emitIFTRUE(label_first, frame))
        self.emit.printout(self.emit.emitLABEL(labelBreak, frame))
        frame.exitLoop()

    def visitFor(self, ast, o):
        #o:any
        #ast.expr1,expr2, expr3: Expr
        #ast.loop: Stmt
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        frame.enterLoop()
        labelContinue = frame.getContinueLabel()
        labelBreak = frame.getBreakLabel()
        label1 = frame.getNewLabel()
        #print(frame.getStackSize())
        str1, typ1 = self.visit(ast.expr1, Access(frame, nenv, False, True))
        self.emit.printout(str1)
        
        self.emit.printout(self.emit.emitLABEL(labelContinue, frame))
        
        str1, typ1 = self.visit(ast.expr2, Access(frame, nenv, False, True))
        self.emit.printout(str1)
        #print(frame.getStackSize())
        self.emit.printout(self.emit.emitIFFALSE(labelBreak, frame))

        #self.visit(ast.loop, o)
        #print(frame.getStackSize())
        if isinstance(ast.loop, Block):
            self.visit(ast.loop, SubBody(frame, [[]] + nenv))
        elif isinstance(ast.loop, Expr) is False:
            self.visit(ast.loop, SubBody(frame, nenv))
        else:
            str1, typ1 = self.visit(ast.loop, Access(frame, nenv, False, True))
            self.emit.printout(str1)
            #print(frame.getStackSize())
            if frame.getStackSize() > 0:
                self.emit.printout(self.emit.emitPOP(frame))
        str1, typ1 = self.visit(ast.expr3, Access(frame, nenv, False, True))
        self.emit.printout(str1)
        self.emit.printout(self.emit.emitGOTO(labelContinue, frame))
        self.emit.printout(self.emit.emitLABEL(labelBreak, frame))
        frame.exitLoop()

    def visitIf(self, ast, o):
        #o:any
        #ast.expr:Expr
        #ast.thenStmt:Stmt
        #ast.elseStmt:Stmt
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        # Kiem tra dieu kien
        #print(frame.getStackSize())
        expr, typ = self.visit(ast.expr, Access(frame, nenv, False, True))
        #print(frame.getStackSize())
        self.emit.printout(expr)
        # label sai
        label1 = frame.getNewLabel()
        # label dung
        label2 = None
        if ast.elseStmt is not None:
            label2 = frame.getNewLabel()
        # Neu dieu kien sai thi nhay toi label1
        self.emit.printout(self.emit.emitIFFALSE(label1, frame))
        #list(map(lambda x: self.visit(x, o), ast.thenStmt))
        if isinstance(ast.thenStmt, Block):
            self.visit(ast.thenStmt, SubBody(frame, [[]] + nenv))
        elif isinstance(ast.thenStmt, Expr) is False:
            self.visit(ast.thenStmt, SubBody(frame, nenv))
        else:
            str1, typ1 = self.visit(ast.thenStmt, Access(frame, nenv, False, True))
            self.emit.printout(str1)
            if frame.getStackSize() > 0:
                self.emit.printout(self.emit.emitPOP(frame))
        #self.visit(ast.thenStmt, Access(frame, nenv, False, True))
        if ast.elseStmt is not None:
            self.emit.printout(self.emit.emitGOTO(label2, frame))
        self.emit.printout(self.emit.emitLABEL(label1,frame))
        if ast.elseStmt is not None:
            #list(map(lambda x: self.visit(x, o), ast.elseStmt))
            #self.visit(ast.elseStmt, o)
            if isinstance(ast.elseStmt, Block):
                self.visit(ast.elseStmt, SubBody(frame, [[]] + nenv))
            elif isinstance(ast.elseStmt, Expr) is False:
                self.visit(ast.elseStmt, SubBody(frame, nenv))
            else:
                str1, typ1 = self.visit(ast.elseStmt, Access(frame, nenv, False, True))
                self.emit.printout(str1)
                if frame.getStackSize() > 0:
                    self.emit.printout(self.emit.emitPOP(frame))
            self.emit.printout(self.emit.emitLABEL(label2, frame))

    def visitBreak(self, ast, o):
        #o:any

        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

    def visitContinue(self, ast, o):
        #o:any
        
        ctxt = o
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

    def visitReturn(self, ast, o):
        #o:any
        #ast.expr: Expr

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        if ast.expr is not None:
            str1, typ1 = self.visit(ast.expr, Access(frame, nenv, False, True))
            if type(typ1) is IntType and type(frame.returnType) is FloatType:
                str1 += self.emit.emitI2F(frame)
            self.emit.printout(str1)
        self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))

    def visitId(self, ast, o):
        #name: str
        sym = None
        for envi in o.sym:
            sym = self.lookup(ast.name, envi, lambda x: x.name)
            if sym is not None:
                break
        typ = sym.mtype
        
        if o.isLeft:
            if type(sym.value) is CName:
                return self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, typ, o.frame), typ
            else:
                return self.emit.emitWRITEVAR(sym.name, typ, sym.value.value, o.frame), typ
        else:
            if type(sym.value) is CName:
                #print(o.frame.getStackSize())
                return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, typ, o.frame), typ
            else:
                return self.emit.emitREADVAR(sym.name, typ, sym.value.value, o.frame), typ

    def visitUnaryOp(self, ast, o):
        #op:str
        #body:Expr
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        body, typ = self.visit(ast.body, Access(frame, nenv, False, True))
        if ast.op.lower() == 'not' and type(typ) is BoolType:
            return body + self.emit.emitNOT(IntType(), frame), BoolType()
        elif ast.op == '-' and type(typ) is IntType:
            return body + self.emit.emitNEGOP(IntType(), frame), IntType()
        elif ast.op == '-' and type(typ) is FloatType:
            return body + self.emit.emitNEGOP(FloatType(), frame), FloatType()

    def Assign(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        if type(ast.left) is ArrayCell:
            # gan mot gia tri cho mot index expression.
            left, typLeft = self.visit(ast.left, Access(frame, nenv, True, True))
            #self.emit.printout(left)
            right, typRight = self.visit(ast.right, Access(frame, nenv, False, True))
            #self.emit.printout(right)
            if type(typLeft) != type(typRight):
                #self.emit.printout(self.emit.emitI2F(frame))
            #self.emit.printout(self.emit.emitASTORE(typLeft, frame))   
                return left + right + self.emitI2F(frame) + self.emit.emitASTORE(typLeft, frame), FloatType()
            else:
                return left + right + self.emit.emitASTORE(typLeft, frame), typLeft
        else:
            # gan mot gia tri cho mot bien
            right, typRight = self.visit(ast.right, Access(frame, nenv, False, True))
            left, typLeft = self.visit(ast.left, Access(frame, nenv, True, True))
            if type(typRight) is IntType and type(typLeft) is FloatType:
                #right += self.emit.emitI2F(frame)
            #self.emit.emitDUP(frame)
            #self.emit.printout(right + left)
                return right + self.emit.emitI2F(frame) + left, FloatType()
            return right + left, typLeft

    def visitBinaryOp(self, ast, o):
        #o: any
        #ast.op:string
        #ast.left:Expr
        #ast.right:Expr
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        if ast.op is '=':
            return self.Assign(ast, o)
        left, typLeft = self.visit(ast.left, Access(frame, nenv, False, True))
        right, typRight = self.visit(ast.right, Access(frame, nenv, False, True))
        
        if type(typLeft) == type(typRight):
            if type(typLeft) is BoolType:
                if ast.op in ['==', '!=']:

                    return left + right + self.emit.emitREOP(ast.op, BoolType(), frame), BoolType()
                elif ast.op == '||':
                    lst = list()
                    lst.append(left)
                    label1 = frame.getNewLabel()
                    label2 = frame.getNewLabel()
                    lst.append(self.emit.emitIFTRUE(label1, frame))
                    lst.append(right)
                    lst.append(self.emit.emitIFTRUE(label1, frame))
                    lst.append(self.emit.emitPUSHICONST(0, frame))
                    lst.append(self.emit.emitGOTO(label2, frame))
                    lst.append(self.emit.emitLABEL(label1, frame))
                    lst.append(self.emit.emitPUSHICONST(1, frame))
                    lst.append(self.emit.emitLABEL(label2, frame))
                    frame.pop()
                    return ''.join(lst), BoolType()
                elif ast.op == '&&':
                    lst = [left]
                    label1 = frame.getNewLabel()
                    label2 = frame.getNewLabel()
                    lst.append(self.emit.emitIFFALSE(label1, frame))
                    lst.append(right)
                    lst.append(self.emit.emitIFFALSE(label1, frame))
                    lst.append(self.emit.emitPUSHICONST(1, frame))
                    lst.append(self.emit.emitGOTO(label2, frame))
                    lst.append(self.emit.emitLABEL(label1, frame))
                    lst.append(self.emit.emitPUSHICONST(0, frame))
                    lst.append(self.emit.emitLABEL(label2, frame))
                    frame.pop()
                    return ''.join(lst), BoolType()

            elif type(typLeft) is IntType:
                if ast.op in ['+', '-']:
                    return left + right + self.emit.emitADDOP(ast.op, IntType(), frame), IntType()
                elif ast.op in ['*', '/']:
                    return left + right + self.emit.emitMULOP(ast.op, IntType(), frame), IntType()
                elif ast.op == '%':
                    return left + right + self.emit.emitMOD(ast.op, IntType(), frame), IntType()
                elif ast.op in ['<', '<=', '>', '>=', '==', '!=']:
                    #print(frame.getStackSize())
                    return left + right + self.emit.emitREOP(ast.op, IntType(), frame), BoolType()

            elif type(typLeft) is FloatType:
                if ast.op in ['+', '-']:
                    return left + right + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
                elif ast.op in ['*', '/']:
                    return left + right + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                elif ast.op in ['<', '<=', '>', '>=']:
                    return self.emit.emitFREOP(ast.op, left, right, frame), BoolType()
            
        else:
            if ast.op in ['+', '-']:
                if type(typLeft) is FloatType and type(typRight) is IntType:
                    return left + right + self.emit.emitI2F(frame) + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
                elif type(typLeft) is IntType and type(typRight) is FloatType:
                    return left + self.emit.emitI2F(frame) + right + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
            elif ast.op in ['*', '/']:
                if type(typLeft) is FloatType and type(typRight) is IntType:
                    return left + right + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                elif type(typLeft) is IntType and type(typRight) is FloatType:
                    return left + self.emit.emitI2F(frame) + right + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
            else:
                if type(typLeft) is IntType: 
                    left += self.emit.emitI2F(frame)
                if type(typRight) is IntType: 
                    right += self.emit.emitI2F(frame)
                if ast.op in ['<', '<=', '>', '>=']:
                    return self.emit.emitFREOP(ast.op, left, right, frame), BoolType()

    def visitArrayCell(self, ast, o):
        #arr:Expr
        #idx:Expr
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        lst = []
        arr, typArr = self.visit(ast.arr, Access(frame, nenv, False, True))
        idx, typIdx = self.visit(ast.idx, Access(frame, nenv, False, True))
        typ = typArr.eleType
        lst.append(arr)
        lst.append(idx)
        if not o.isLeft:
            lst.append(self.emit.emitALOAD(typ, frame))
            
        return ''.join(lst), typ

    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv[-1], lambda x: x.name)
        cname = sym.value.value
        ctype = sym.mtype

        in_ = ("", list())
        for i in range(len(ast.param)):
            str1, typ1 = self.visit(ast.param[i], Access(frame, nenv, False, True))
            if type(typ1) is IntType and type(sym.mtype.partype[i]) is FloatType:
                str1 += self.emit.emitI2F(frame)
            in_ = (in_[0] + str1, in_[1].append(typ1))
        #in_[0] += self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame)
        #self.emit.printout(in_[0])
        #self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))
        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame), ctype.rettype

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(int(ast.value), frame), BoolType()
    
    def visitStringLiteral(self, ast, o):
        #o:any
        #ast.value:string
        
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()