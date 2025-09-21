# Generated from grammar/CppParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CppParser import CppParser
else:
    from CppParser import CppParser

# This class defines a complete listener for a parse tree produced by CppParser.
class CppParserListener(ParseTreeListener):

    # Enter a parse tree produced by CppParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CppParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CppParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CppParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by CppParser#translationUnit.
    def enterTranslationUnit(self, ctx:CppParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by CppParser#translationUnit.
    def exitTranslationUnit(self, ctx:CppParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by CppParser#namespaceDefinition.
    def enterNamespaceDefinition(self, ctx:CppParser.NamespaceDefinitionContext):
        pass

    # Exit a parse tree produced by CppParser#namespaceDefinition.
    def exitNamespaceDefinition(self, ctx:CppParser.NamespaceDefinitionContext):
        pass


    # Enter a parse tree produced by CppParser#classDefinition.
    def enterClassDefinition(self, ctx:CppParser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by CppParser#classDefinition.
    def exitClassDefinition(self, ctx:CppParser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by CppParser#classKey.
    def enterClassKey(self, ctx:CppParser.ClassKeyContext):
        pass

    # Exit a parse tree produced by CppParser#classKey.
    def exitClassKey(self, ctx:CppParser.ClassKeyContext):
        pass


    # Enter a parse tree produced by CppParser#classInheritanceList.
    def enterClassInheritanceList(self, ctx:CppParser.ClassInheritanceListContext):
        pass

    # Exit a parse tree produced by CppParser#classInheritanceList.
    def exitClassInheritanceList(self, ctx:CppParser.ClassInheritanceListContext):
        pass


    # Enter a parse tree produced by CppParser#classInheritance.
    def enterClassInheritance(self, ctx:CppParser.ClassInheritanceContext):
        pass

    # Exit a parse tree produced by CppParser#classInheritance.
    def exitClassInheritance(self, ctx:CppParser.ClassInheritanceContext):
        pass


    # Enter a parse tree produced by CppParser#classBody.
    def enterClassBody(self, ctx:CppParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by CppParser#classBody.
    def exitClassBody(self, ctx:CppParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by CppParser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:CppParser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by CppParser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:CppParser.AccessSpecifierContext):
        pass


    # Enter a parse tree produced by CppParser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:CppParser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by CppParser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:CppParser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by CppParser#staticDeclaration.
    def enterStaticDeclaration(self, ctx:CppParser.StaticDeclarationContext):
        pass

    # Exit a parse tree produced by CppParser#staticDeclaration.
    def exitStaticDeclaration(self, ctx:CppParser.StaticDeclarationContext):
        pass


    # Enter a parse tree produced by CppParser#virtualDeclaration.
    def enterVirtualDeclaration(self, ctx:CppParser.VirtualDeclarationContext):
        pass

    # Exit a parse tree produced by CppParser#virtualDeclaration.
    def exitVirtualDeclaration(self, ctx:CppParser.VirtualDeclarationContext):
        pass


    # Enter a parse tree produced by CppParser#friendDeclaration.
    def enterFriendDeclaration(self, ctx:CppParser.FriendDeclarationContext):
        pass

    # Exit a parse tree produced by CppParser#friendDeclaration.
    def exitFriendDeclaration(self, ctx:CppParser.FriendDeclarationContext):
        pass


    # Enter a parse tree produced by CppParser#templateDeclaration.
    def enterTemplateDeclaration(self, ctx:CppParser.TemplateDeclarationContext):
        pass

    # Exit a parse tree produced by CppParser#templateDeclaration.
    def exitTemplateDeclaration(self, ctx:CppParser.TemplateDeclarationContext):
        pass


    # Enter a parse tree produced by CppParser#templateParameterList.
    def enterTemplateParameterList(self, ctx:CppParser.TemplateParameterListContext):
        pass

    # Exit a parse tree produced by CppParser#templateParameterList.
    def exitTemplateParameterList(self, ctx:CppParser.TemplateParameterListContext):
        pass


    # Enter a parse tree produced by CppParser#templateParameter.
    def enterTemplateParameter(self, ctx:CppParser.TemplateParameterContext):
        pass

    # Exit a parse tree produced by CppParser#templateParameter.
    def exitTemplateParameter(self, ctx:CppParser.TemplateParameterContext):
        pass


    # Enter a parse tree produced by CppParser#memberFunction.
    def enterMemberFunction(self, ctx:CppParser.MemberFunctionContext):
        pass

    # Exit a parse tree produced by CppParser#memberFunction.
    def exitMemberFunction(self, ctx:CppParser.MemberFunctionContext):
        pass


    # Enter a parse tree produced by CppParser#returnType.
    def enterReturnType(self, ctx:CppParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by CppParser#returnType.
    def exitReturnType(self, ctx:CppParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by CppParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CppParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CppParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CppParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CppParser#templateArgumentList.
    def enterTemplateArgumentList(self, ctx:CppParser.TemplateArgumentListContext):
        pass

    # Exit a parse tree produced by CppParser#templateArgumentList.
    def exitTemplateArgumentList(self, ctx:CppParser.TemplateArgumentListContext):
        pass


    # Enter a parse tree produced by CppParser#templateArgument.
    def enterTemplateArgument(self, ctx:CppParser.TemplateArgumentContext):
        pass

    # Exit a parse tree produced by CppParser#templateArgument.
    def exitTemplateArgument(self, ctx:CppParser.TemplateArgumentContext):
        pass


    # Enter a parse tree produced by CppParser#functionName.
    def enterFunctionName(self, ctx:CppParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by CppParser#functionName.
    def exitFunctionName(self, ctx:CppParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by CppParser#operatorName.
    def enterOperatorName(self, ctx:CppParser.OperatorNameContext):
        pass

    # Exit a parse tree produced by CppParser#operatorName.
    def exitOperatorName(self, ctx:CppParser.OperatorNameContext):
        pass


    # Enter a parse tree produced by CppParser#operatorSymbol.
    def enterOperatorSymbol(self, ctx:CppParser.OperatorSymbolContext):
        pass

    # Exit a parse tree produced by CppParser#operatorSymbol.
    def exitOperatorSymbol(self, ctx:CppParser.OperatorSymbolContext):
        pass


    # Enter a parse tree produced by CppParser#parameterList.
    def enterParameterList(self, ctx:CppParser.ParameterListContext):
        pass

    # Exit a parse tree produced by CppParser#parameterList.
    def exitParameterList(self, ctx:CppParser.ParameterListContext):
        pass


    # Enter a parse tree produced by CppParser#parameter.
    def enterParameter(self, ctx:CppParser.ParameterContext):
        pass

    # Exit a parse tree produced by CppParser#parameter.
    def exitParameter(self, ctx:CppParser.ParameterContext):
        pass


    # Enter a parse tree produced by CppParser#defaultValue.
    def enterDefaultValue(self, ctx:CppParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by CppParser#defaultValue.
    def exitDefaultValue(self, ctx:CppParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by CppParser#memberVariable.
    def enterMemberVariable(self, ctx:CppParser.MemberVariableContext):
        pass

    # Exit a parse tree produced by CppParser#memberVariable.
    def exitMemberVariable(self, ctx:CppParser.MemberVariableContext):
        pass


    # Enter a parse tree produced by CppParser#constructor.
    def enterConstructor(self, ctx:CppParser.ConstructorContext):
        pass

    # Exit a parse tree produced by CppParser#constructor.
    def exitConstructor(self, ctx:CppParser.ConstructorContext):
        pass


    # Enter a parse tree produced by CppParser#destructor.
    def enterDestructor(self, ctx:CppParser.DestructorContext):
        pass

    # Exit a parse tree produced by CppParser#destructor.
    def exitDestructor(self, ctx:CppParser.DestructorContext):
        pass


    # Enter a parse tree produced by CppParser#memberInitializerList.
    def enterMemberInitializerList(self, ctx:CppParser.MemberInitializerListContext):
        pass

    # Exit a parse tree produced by CppParser#memberInitializerList.
    def exitMemberInitializerList(self, ctx:CppParser.MemberInitializerListContext):
        pass


    # Enter a parse tree produced by CppParser#memberInitializer.
    def enterMemberInitializer(self, ctx:CppParser.MemberInitializerContext):
        pass

    # Exit a parse tree produced by CppParser#memberInitializer.
    def exitMemberInitializer(self, ctx:CppParser.MemberInitializerContext):
        pass


    # Enter a parse tree produced by CppParser#argumentList.
    def enterArgumentList(self, ctx:CppParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by CppParser#argumentList.
    def exitArgumentList(self, ctx:CppParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by CppParser#argument.
    def enterArgument(self, ctx:CppParser.ArgumentContext):
        pass

    # Exit a parse tree produced by CppParser#argument.
    def exitArgument(self, ctx:CppParser.ArgumentContext):
        pass


    # Enter a parse tree produced by CppParser#inlineMethod.
    def enterInlineMethod(self, ctx:CppParser.InlineMethodContext):
        pass

    # Exit a parse tree produced by CppParser#inlineMethod.
    def exitInlineMethod(self, ctx:CppParser.InlineMethodContext):
        pass


    # Enter a parse tree produced by CppParser#methodWithBody.
    def enterMethodWithBody(self, ctx:CppParser.MethodWithBodyContext):
        pass

    # Exit a parse tree produced by CppParser#methodWithBody.
    def exitMethodWithBody(self, ctx:CppParser.MethodWithBodyContext):
        pass


    # Enter a parse tree produced by CppParser#methodBody.
    def enterMethodBody(self, ctx:CppParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by CppParser#methodBody.
    def exitMethodBody(self, ctx:CppParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by CppParser#constructorBody.
    def enterConstructorBody(self, ctx:CppParser.ConstructorBodyContext):
        pass

    # Exit a parse tree produced by CppParser#constructorBody.
    def exitConstructorBody(self, ctx:CppParser.ConstructorBodyContext):
        pass


    # Enter a parse tree produced by CppParser#destructorBody.
    def enterDestructorBody(self, ctx:CppParser.DestructorBodyContext):
        pass

    # Exit a parse tree produced by CppParser#destructorBody.
    def exitDestructorBody(self, ctx:CppParser.DestructorBodyContext):
        pass


    # Enter a parse tree produced by CppParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CppParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CppParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CppParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CppParser#functionBody.
    def enterFunctionBody(self, ctx:CppParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by CppParser#functionBody.
    def exitFunctionBody(self, ctx:CppParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by CppParser#usingDeclaration.
    def enterUsingDeclaration(self, ctx:CppParser.UsingDeclarationContext):
        pass

    # Exit a parse tree produced by CppParser#usingDeclaration.
    def exitUsingDeclaration(self, ctx:CppParser.UsingDeclarationContext):
        pass


    # Enter a parse tree produced by CppParser#preprocessorDirective.
    def enterPreprocessorDirective(self, ctx:CppParser.PreprocessorDirectiveContext):
        pass

    # Exit a parse tree produced by CppParser#preprocessorDirective.
    def exitPreprocessorDirective(self, ctx:CppParser.PreprocessorDirectiveContext):
        pass



del CppParser