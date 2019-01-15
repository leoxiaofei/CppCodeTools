# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frmCppCodeTools
###########################################################################

class frmCppCodeTools ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CppCodeTools", pos = wx.DefaultPosition, size = wx.Size( 792,599 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		sizerMain = wx.BoxSizer( wx.HORIZONTAL )

		self.lbPage = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )

		sizerMain.Add( self.lbPage, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( sizerMain )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class frmStringToEnum
###########################################################################

class frmStringToEnum ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = 0, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizerMain = wx.BoxSizer( wx.HORIZONTAL )

		sbSizerString = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"String" ), wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lblWrap = wx.StaticText( sbSizerString.GetStaticBox(), wx.ID_ANY, u"Wrap:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblWrap.Wrap( -1 )

		fgSizer1.Add( self.lblWrap, 0, wx.ALL, 5 )

		self.cbWrap = wx.CheckBox( sbSizerString.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbWrap.SetValue(True)
		fgSizer1.Add( self.cbWrap, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lblPrefix = wx.StaticText( sbSizerString.GetStaticBox(), wx.ID_ANY, u"Prefix:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPrefix.Wrap( -1 )

		fgSizer1.Add( self.lblPrefix, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.edtPrefix = wx.TextCtrl( sbSizerString.GetStaticBox(), wx.ID_ANY, u"_", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.edtPrefix, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizerString.Add( fgSizer1, 0, wx.EXPAND, 5 )

		self.edtString = wx.TextCtrl( sbSizerString.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerString.Add( self.edtString, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerString, 1, wx.EXPAND, 5 )

		sbSizerEnum = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Enum" ), wx.VERTICAL )

		self.edtEnum = wx.TextCtrl( sbSizerEnum.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerEnum.Add( self.edtEnum, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerEnum, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerMain )
		self.Layout()

		# Connect Events
		self.cbWrap.Bind( wx.EVT_CHECKBOX, self.OnCheckCbWrap )
		self.edtPrefix.Bind( wx.EVT_TEXT, self.OnTextEdtPrefix )
		self.edtString.Bind( wx.EVT_TEXT, self.OnTextEdtString )

	def __del__( self ):
		# Disconnect Events
		self.cbWrap.Unbind( wx.EVT_CHECKBOX, handler = self.OnCheckCbWrap )
		self.edtPrefix.Unbind( wx.EVT_TEXT, handler = self.OnTextEdtPrefix )
		self.edtString.Unbind( wx.EVT_TEXT, handler = self.OnTextEdtString )


	# Virtual event handlers, overide them in your derived class
	def OnCheckCbWrap( self, event ):
		event.Skip()

	def OnTextEdtPrefix( self, event ):
		event.Skip()

	def OnTextEdtString( self, event ):
		event.Skip()


###########################################################################
## Class frmEnumToSwitch
###########################################################################

class frmEnumToSwitch ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizerMain = wx.BoxSizer( wx.HORIZONTAL )

		sbSizerEnum = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Enum" ), wx.VERTICAL )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lblExpValue = wx.StaticText( sbSizerEnum.GetStaticBox(), wx.ID_ANY, u"ExpValue:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblExpValue.Wrap( -1 )

		fgSizer2.Add( self.lblExpValue, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.edtExpValue = wx.TextCtrl( sbSizerEnum.GetStaticBox(), wx.ID_ANY, u"eType", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.edtExpValue, 0, wx.ALL, 5 )

		self.lblNamespace = wx.StaticText( sbSizerEnum.GetStaticBox(), wx.ID_ANY, u"Namespace:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNamespace.Wrap( -1 )

		fgSizer2.Add( self.lblNamespace, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.edtNamespace = wx.TextCtrl( sbSizerEnum.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.edtNamespace, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lblBreak = wx.StaticText( sbSizerEnum.GetStaticBox(), wx.ID_ANY, u"Has Break:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblBreak.Wrap( -1 )

		fgSizer2.Add( self.lblBreak, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.cbBreak = wx.CheckBox( sbSizerEnum.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbBreak.SetValue(True)
		fgSizer2.Add( self.cbBreak, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizerEnum.Add( fgSizer2, 0, wx.EXPAND, 5 )

		self.edtEnum = wx.TextCtrl( sbSizerEnum.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerEnum.Add( self.edtEnum, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerEnum, 1, wx.EXPAND, 5 )

		sbSizerSwitch = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Switch" ), wx.VERTICAL )

		self.edtSwitch = wx.TextCtrl( sbSizerSwitch.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerSwitch.Add( self.edtSwitch, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerSwitch, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerMain )
		self.Layout()

		# Connect Events
		self.edtExpValue.Bind( wx.EVT_TEXT, self.OnTextEdtExpValue )
		self.edtNamespace.Bind( wx.EVT_TEXT, self.OnTextEdtNamespace )
		self.cbBreak.Bind( wx.EVT_CHECKBOX, self.OnCheckCbBreak )
		self.edtEnum.Bind( wx.EVT_TEXT, self.OnTextEdtEnum )

	def __del__( self ):
		# Disconnect Events
		self.edtExpValue.Unbind( wx.EVT_TEXT, handler = self.OnTextEdtExpValue )
		self.edtNamespace.Unbind( wx.EVT_TEXT, handler = self.OnTextEdtNamespace )
		self.cbBreak.Unbind( wx.EVT_CHECKBOX, handler = self.OnCheckCbBreak )
		self.edtEnum.Unbind( wx.EVT_TEXT, handler = self.OnTextEdtEnum )


	# Virtual event handlers, overide them in your derived class
	def OnTextEdtExpValue( self, event ):
		event.Skip()

	def OnTextEdtNamespace( self, event ):
		event.Skip()

	def OnCheckCbBreak( self, event ):
		event.Skip()

	def OnTextEdtEnum( self, event ):
		event.Skip()


###########################################################################
## Class frmNameToClass
###########################################################################

class frmNameToClass ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 671,507 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizerMain = wx.BoxSizer( wx.HORIZONTAL )

		sbSizerIn = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"In" ), wx.VERTICAL )

		fgSizerIn = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizerIn.SetFlexibleDirection( wx.BOTH )
		fgSizerIn.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lblClassName = wx.StaticText( sbSizerIn.GetStaticBox(), wx.ID_ANY, u"ClassName:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblClassName.Wrap( -1 )

		fgSizerIn.Add( self.lblClassName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.edtClassName = wx.TextCtrl( sbSizerIn.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerIn.Add( self.edtClassName, 0, wx.ALL, 5 )

		self.lblClassBase = wx.StaticText( sbSizerIn.GetStaticBox(), wx.ID_ANY, u"ClassBase:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblClassBase.Wrap( -1 )

		fgSizerIn.Add( self.lblClassBase, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.edtClassBase = wx.TextCtrl( sbSizerIn.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerIn.Add( self.edtClassBase, 0, wx.ALL, 5 )

		self.lblImpl = wx.StaticText( sbSizerIn.GetStaticBox(), wx.ID_ANY, u"Impl:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblImpl.Wrap( -1 )

		fgSizerIn.Add( self.lblImpl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.cbImpl = wx.CheckBox( sbSizerIn.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbImpl.SetValue(True)
		fgSizerIn.Add( self.cbImpl, 0, wx.ALL, 5 )

		self.lblSharedPtr = wx.StaticText( sbSizerIn.GetStaticBox(), wx.ID_ANY, u"SharedPtr:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblSharedPtr.Wrap( -1 )

		fgSizerIn.Add( self.lblSharedPtr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.edtSharedPtr = wx.TextCtrl( sbSizerIn.GetStaticBox(), wx.ID_ANY, u"QScopedPointer", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerIn.Add( self.edtSharedPtr, 0, wx.ALL, 5 )

		self.lblQObject = wx.StaticText( sbSizerIn.GetStaticBox(), wx.ID_ANY, u"Q_OBJECT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblQObject.Wrap( -1 )

		fgSizerIn.Add( self.lblQObject, 0, wx.ALL, 5 )

		self.cbQObject = wx.CheckBox( sbSizerIn.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerIn.Add( self.cbQObject, 0, wx.ALL, 5 )


		sbSizerIn.Add( fgSizerIn, 1, wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerIn, 1, wx.EXPAND, 5 )

		sbSizerOut = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Out" ), wx.VERTICAL )

		self.lblH = wx.StaticText( sbSizerOut.GetStaticBox(), wx.ID_ANY, u".h", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblH.Wrap( -1 )

		sbSizerOut.Add( self.lblH, 0, wx.ALL, 5 )

		self.edtH = wx.TextCtrl( sbSizerOut.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerOut.Add( self.edtH, 1, wx.ALL|wx.EXPAND, 5 )

		self.lblCpp = wx.StaticText( sbSizerOut.GetStaticBox(), wx.ID_ANY, u".cpp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblCpp.Wrap( -1 )

		sbSizerOut.Add( self.lblCpp, 0, wx.ALL|wx.EXPAND, 5 )

		self.edtCpp = wx.TextCtrl( sbSizerOut.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerOut.Add( self.edtCpp, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerOut, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerMain )
		self.Layout()

		# Connect Events
		self.edtClassName.Bind( wx.EVT_TEXT, self.OnTextEdtClassName )
		self.edtClassBase.Bind( wx.EVT_TEXT, self.OnTextEdtClassBase )
		self.cbImpl.Bind( wx.EVT_CHECKBOX, self.OnCheckCbImpl )
		self.edtSharedPtr.Bind( wx.EVT_TEXT, self.OnTextEdtSharedPtr )
		self.cbQObject.Bind( wx.EVT_CHECKBOX, self.OnCheckCbQObject )

	def __del__( self ):
		# Disconnect Events
		self.edtClassName.Unbind( wx.EVT_TEXT, handler = self.OnTextEdtClassName )
		self.edtClassBase.Unbind( wx.EVT_TEXT, handler = self.OnTextEdtClassBase )
		self.cbImpl.Unbind( wx.EVT_CHECKBOX, handler = self.OnCheckCbImpl )
		self.edtSharedPtr.Unbind( wx.EVT_TEXT, handler = self.OnTextEdtSharedPtr )
		self.cbQObject.Unbind( wx.EVT_CHECKBOX, handler = self.OnCheckCbQObject )


	# Virtual event handlers, overide them in your derived class
	def OnTextEdtClassName( self, event ):
		event.Skip()

	def OnTextEdtClassBase( self, event ):
		event.Skip()

	def OnCheckCbImpl( self, event ):
		event.Skip()

	def OnTextEdtSharedPtr( self, event ):
		event.Skip()

	def OnCheckCbQObject( self, event ):
		event.Skip()


###########################################################################
## Class frmQtClassToHeader
###########################################################################

class frmQtClassToHeader ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizerMain = wx.BoxSizer( wx.HORIZONTAL )

		sbSizerClass = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Class" ), wx.VERTICAL )

		self.edtClass = wx.TextCtrl( sbSizerClass.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerClass.Add( self.edtClass, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerClass, 1, wx.EXPAND, 5 )

		sbSizerHeader = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Header" ), wx.VERTICAL )

		self.edtHeader = wx.TextCtrl( sbSizerHeader.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerHeader.Add( self.edtHeader, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerHeader, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerMain )
		self.Layout()

		# Connect Events
		self.edtClass.Bind( wx.EVT_TEXT, self.OnTextClass )

	def __del__( self ):
		# Disconnect Events
		self.edtClass.Unbind( wx.EVT_TEXT, handler = self.OnTextClass )


	# Virtual event handlers, overide them in your derived class
	def OnTextClass( self, event ):
		event.Skip()


###########################################################################
## Class frmXmlPicker
###########################################################################

class frmXmlPicker ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizerMain = wx.BoxSizer( wx.HORIZONTAL )

		sbSizerXml = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"XML" ), wx.VERTICAL )

		self.edtXml = wx.TextCtrl( sbSizerXml.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerXml.Add( self.edtXml, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerXml, 1, wx.EXPAND, 5 )

		sbSizerResult = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Result" ), wx.VERTICAL )

		self.edtRes = wx.TextCtrl( sbSizerResult.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerResult.Add( self.edtRes, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerResult, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerMain )
		self.Layout()

		# Connect Events
		self.edtXml.Bind( wx.EVT_TEXT, self.OnTextXml )

	def __del__( self ):
		# Disconnect Events
		self.edtXml.Unbind( wx.EVT_TEXT, handler = self.OnTextXml )


	# Virtual event handlers, overide them in your derived class
	def OnTextXml( self, event ):
		event.Skip()


###########################################################################
## Class frmJsonPicker
###########################################################################

class frmJsonPicker ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizerMain = wx.BoxSizer( wx.HORIZONTAL )

		sbSizerJson = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Json" ), wx.VERTICAL )

		self.edtJson = wx.TextCtrl( sbSizerJson.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerJson.Add( self.edtJson, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerJson, 1, wx.EXPAND, 5 )

		sbSizerResult = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Result" ), wx.VERTICAL )

		self.edtRes = wx.TextCtrl( sbSizerResult.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerResult.Add( self.edtRes, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerResult, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerMain )
		self.Layout()

		# Connect Events
		self.edtJson.Bind( wx.EVT_TEXT, self.OnTextJson )

	def __del__( self ):
		# Disconnect Events
		self.edtJson.Unbind( wx.EVT_TEXT, handler = self.OnTextJson )


	# Virtual event handlers, overide them in your derived class
	def OnTextJson( self, event ):
		event.Skip()


###########################################################################
## Class frmDeclToMen
###########################################################################

class frmDeclToMen ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizerMain = wx.BoxSizer( wx.HORIZONTAL )

		sbSizerDecl = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Declaration" ), wx.VERTICAL )

		fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.lblObject = wx.StaticText( sbSizerDecl.GetStaticBox(), wx.ID_ANY, u"&Object:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblObject.Wrap( -1 )

		fgSizer4.Add( self.lblObject, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.edtObject = wx.TextCtrl( sbSizerDecl.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.edtObject, 1, wx.ALL|wx.EXPAND, 5 )

		self.cbtnPtr = wx.CheckBox( sbSizerDecl.GetStaticBox(), wx.ID_ANY, u"IsPtr", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.cbtnPtr, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		sbSizerDecl.Add( fgSizer4, 0, wx.EXPAND, 5 )

		self.edtDecl = wx.TextCtrl( sbSizerDecl.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerDecl.Add( self.edtDecl, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerDecl, 1, wx.EXPAND, 5 )

		sbSizerMember = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Membar" ), wx.VERTICAL )

		self.edtMember = wx.TextCtrl( sbSizerMember.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizerMember.Add( self.edtMember, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerMain.Add( sbSizerMember, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizerMain )
		self.Layout()

		# Connect Events
		self.edtObject.Bind( wx.EVT_TEXT, self.OnTextObject )
		self.cbtnPtr.Bind( wx.EVT_CHECKBOX, self.OnCheckPtr )
		self.edtDecl.Bind( wx.EVT_TEXT, self.OnTextDecl )

	def __del__( self ):
		# Disconnect Events
		self.edtObject.Unbind( wx.EVT_TEXT, handler = self.OnTextObject )
		self.cbtnPtr.Unbind( wx.EVT_CHECKBOX, handler = self.OnCheckPtr )
		self.edtDecl.Unbind( wx.EVT_TEXT, handler = self.OnTextDecl )


	# Virtual event handlers, overide them in your derived class
	def OnTextObject( self, event ):
		event.Skip()

	def OnCheckPtr( self, event ):
		event.Skip()

	def OnTextDecl( self, event ):
		event.Skip()


