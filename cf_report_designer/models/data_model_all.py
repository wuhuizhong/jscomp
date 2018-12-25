# -*- coding: utf-8 -*-
# 康虎软件工作室
# http://www.khcloud.net
# QQ: 360026606
# wechat: 360026606
#--------------------------
#
import os
import sys
import logging
import string
try :
 import simplejson as json
except ImportError :
 import json
 if 64 - 64: i11iIiiIii
from lxml import etree
try :
 import xml . etree . cElementTree as ET
except ImportError :
 import xml . etree . ElementTree as ET
from xml . dom import minidom
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
from odoo . exceptions import AccessError , UserError , ValidationError
from odoo import models , fields , api , _
from Crypto . Cipher import AES
if 73 - 73: II111iiii
IiII1IiiIiI1 = logging . getLogger ( __name__ )
if 40 - 40: oo * OoO0O00
if 2 - 2: ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o . oOoO0oo0OOOo + iiiiIi11i
import os
import sys
import hashlib
import string
import random
import base64
from binascii import b2a_hex , a2b_hex
if 24 - 24: II11iiII / OoOO0ooOOoo0O + o0000oOoOoO0o * i1I1ii1II1iII % oooO0oo0oOOOO
from Crypto import Random
from Crypto . Cipher import AES
if 53 - 53: o0oo0o / Oo + o0oo0o / oooO0oo0oOOOO * OoooooooOO + i1I1ii1II1iII
OOo0oO0oooOoO = ( 'C' )
ooO00oOoo = ( 'FS' )
O0OOo = ( 'O' )
II1Iiii1111i = ( 'F' )
i1IIi11111i = ( 'T' )
o000o0o00o0Oo = ( 'S' )
if 80 - 80: OoooooooOO . oo
OOO0O = ( 't' )
oo0ooO0oOOOOo = ( 'u' )
oO000OoOoo00o = ( 'd' )
iiiI11 = ( 'i' )
OOooO = ( 'o72' )
OOoO00o = ( '0' )
II111iiiiII = ( '1' )
if 63 - 63: oOo0O0Ooo % i1IIi
o0oOo0Ooo0O = b"1234567890123456"
if 81 - 81: oOoO0oo0OOOo * oooO0oo0oOOOO * OoOO0ooOOoo0O - i1I1ii1II1iII - Ooo00oOo00o
def OooO0OO ( ) :
 return '' . join ( OOo0oO0oooOoO + ooO00oOoo + O0OOo + II1Iiii1111i + i1IIi11111i + o000o0o00o0Oo + OOO0O + oo0ooO0oOOOOo + oO000OoOoo00o + iiiI11 + OOooO + OOoO00o + II111iiiiII )
 if 28 - 28: II111iiii
 if 28 - 28: iIii1I11I1II1 - i1IIi
OO = len ( OooO0OO ( ) )
oO0O = lambda OOoO000O0OO : OOoO000O0OO + ( OO - len ( OOoO000O0OO ) % OO ) * chr ( OO - len ( OOoO000O0OO ) % OO )
iiI1IiI = lambda OOoO000O0OO : OOoO000O0OO [ 0 : - ord ( OOoO000O0OO [ - 1 ] ) ]
if 13 - 13: OoO0O00 . i11iIiiIii - iIii1I11I1II1 - oOo0O0Ooo
class ii1I ( object ) :
 def __init__ ( self , key = False , mode = AES . MODE_CBC ) :
  if 76 - 76: O0 / Ooo00oOo00o . oo * o0000oOoOoO0o - II11iiII
  if 76 - 76: i11iIiiIii / iIii1I11I1II1 . oOoO0oo0OOOo % II11iiII / OoooooooOO % iiiiIi11i
  if 75 - 75: i1I1ii1II1iII
  if 97 - 97: i11iIiiIii
  if 32 - 32: OoO0O00 * O0 % iiiiIi11i % o0000oOoOoO0o . oooO0oo0oOOOO
  if 61 - 61: Oo
  if 79 - 79: OoO0O00 + oo - i1I1ii1II1iII
  if 83 - 83: Oo
  if 64 - 64: ooOO00oOo % Oo % i1I1ii1II1iII / oOo0O0Ooo - ooOO00oOo
  if 74 - 74: i1I1ii1II1iII * O0
  if 89 - 89: iiiiIi11i + OoO0O00
  if 3 - 3: i1IIi / oo % OoOO0ooOOoo0O * i11iIiiIii / O0 * OoOO0ooOOoo0O
  if 49 - 49: iiiiIi11i % o0000oOoOoO0o + i1IIi . oo % oOoO0oo0OOOo
  if 48 - 48: OoOO0ooOOoo0O + OoOO0ooOOoo0O / II111iiii / iIii1I11I1II1
  self . key = key or OooO0OO ( )
  self . mode = mode
  self . key = self . key . encode ( 'utf-8' )
  if 20 - 20: Ooo00oOo00o
 @ staticmethod
 def get_machine_code ( ) :
  import uuid
  if 77 - 77: oOo0O0Ooo / OoOO0ooOOoo0O
  return str ( uuid . UUID ( int = uuid . getnode ( ) ) )
  if 98 - 98: iIii1I11I1II1 / i1IIi / i11iIiiIii / Ooo00oOo00o
 @ staticmethod
 def rand_aes_key ( size = 16 , by_base64 = True , chars = string . ascii_uppercase + string . digits ) :
  I1i1I1II = '' . join ( random . choice ( chars ) for _ in range ( size ) )
  if 45 - 45: o0oo0o . oOo0O0Ooo
  if 83 - 83: iiiiIi11i . iIii1I11I1II1 . oOoO0oo0OOOo
  if 31 - 31: o0000oOoOoO0o . o0000oOoOoO0o - Ooo00oOo00o / ooOO00oOo + Oo * oo
  if 63 - 63: o0oo0o % i1IIi / OoooooooOO - OoooooooOO
  if 8 - 8: oOo0O0Ooo
  if 60 - 60: OoOO0ooOOoo0O / OoOO0ooOOoo0O
  return base64 . b64encode ( I1i1I1II ) if by_base64 else I1i1I1II
  if 46 - 46: o0000oOoOoO0o * II11iiII - ooOO00oOo * iiiiIi11i - o0oo0o
  if 83 - 83: OoooooooOO
 def encrypt ( self , text ) :
  text = oO0O ( text ) . encode ( 'utf-8' )
  Iii111II = AES . new ( self . key , self . mode , o0oOo0Ooo0O )
  self . ciphertext = Iii111II . encrypt ( text )
  if 9 - 9: ooOO00oOo
  return base64 . b64encode ( self . ciphertext )
  if 33 - 33: Oo . i1I1ii1II1iII
  if 58 - 58: II11iiII * i11iIiiIii / oOo0O0Ooo % o0oo0o - oOoO0oo0OOOo / iiiiIi11i
 def decrypt ( self , text ) :
  ii11i1 = base64 . b64decode ( text )
  Iii111II = AES . new ( self . key , self . mode , o0oOo0Ooo0O )
  if 29 - 29: oOoO0oo0OOOo % oo + Oo / Ooo00oOo00o + II11iiII * Ooo00oOo00o
  if 42 - 42: o0000oOoOoO0o + iiiiIi11i
  o0O0o0Oo = bytes . decode ( Iii111II . decrypt ( ii11i1 ) )
  return iiI1IiI ( o0O0o0Oo )
  if 16 - 16: O0 - o0oo0o * iIii1I11I1II1 + i1I1ii1II1iII
  if 50 - 50: II111iiii - Oo * oOoO0oo0OOOo / o0oo0o + Ooo00oOo00o
from Crypto import Random
from Crypto . Hash import SHA
from Crypto . Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto . Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto . PublicKey import RSA
if 88 - 88: o0000oOoOoO0o / o0oo0o + i1I1ii1II1iII - II111iiii / Oo - oOo0O0Ooo
class IIIIii ( ) :
 if 70 - 70: o0000oOoOoO0o / OoOO0ooOOoo0O . i1I1ii1II1iII % OoO0O00
 if 67 - 67: oOo0O0Ooo * Ooo00oOo00o . oooO0oo0oOOOO - ooOO00oOo * Ooo00oOo00o
 if 46 - 46: II11iiII + oOo0O0Ooo . oo * iiiiIi11i % oooO0oo0oOOOO
 if 86 - 86: oo + o0000oOoOoO0o % i11iIiiIii * iiiiIi11i . Oo * OoOO0ooOOoo0O
 if 44 - 44: iiiiIi11i
 if 88 - 88: o0oo0o % o0000oOoOoO0o . II111iiii
 if 38 - 38: Ooo00oOo00o
 if 57 - 57: O0 / iiiiIi11i * o0oo0o / oOo0O0Ooo . II111iiii
 if 26 - 26: i1I1ii1II1iII
 if 91 - 91: ooOO00oOo . oOoO0oo0OOOo + ooOO00oOo - i1I1ii1II1iII / OoooooooOO
 if 39 - 39: oOoO0oo0OOOo / Oo - II111iiii
 if 98 - 98: oOoO0oo0OOOo / OoOO0ooOOoo0O % iiiiIi11i . oOo0O0Ooo
 if 91 - 91: iiiiIi11i % OoO0O00
 if 64 - 64: OoOO0ooOOoo0O % i1I1ii1II1iII - o0oo0o - iiiiIi11i
 if 31 - 31: OoOO0ooOOoo0O - II111iiii . OoOO0ooOOoo0O
 def __init__ ( self , pri_key = 'pri.pem' , pub_key = 'pub.pem' , key_path = os . path . abspath ( os . path . dirname ( __file__ ) ) ) :
  self . KEY_PRIVATE = pri_key
  self . KEY_PUBLIC = pub_key
  self . KEY_PATH = key_path
  if 18 - 18: Ooo00oOo00o
 def gen_key_pair ( self ) :
  if 98 - 98: i1I1ii1II1iII * i1I1ii1II1iII / i1I1ii1II1iII + OoOO0ooOOoo0O
  ii111111I1iII = Random . new ( ) . read
  if 68 - 68: i1I1ii1II1iII - iIii1I11I1II1 * i11iIiiIii / oOoO0oo0OOOo * o0oo0o
  i1iIi1iIi1i = RSA . generate ( 1024 , ii111111I1iII )
  if 46 - 46: o0oo0o % OoOO0ooOOoo0O + ooOO00oOo . oOo0O0Ooo . ooOO00oOo
  if 96 - 96: OoO0O00
  Ii1I1IIii1II = i1iIi1iIi1i . exportKey ( )
  if 65 - 65: o0000oOoOoO0o . iIii1I11I1II1 / O0 - o0000oOoOoO0o
  with open ( self . KEY_PATH + "/" + self . KEY_PRIVATE , 'w' ) as iii1i1iiiiIi :
   iii1i1iiiiIi . write ( Ii1I1IIii1II )
   if 2 - 2: oo / O0 / Ooo00oOo00o % oOo0O0Ooo % o0000oOoOoO0o
  o0o00OO0 = i1iIi1iIi1i . publickey ( ) . exportKey ( )
  with open ( self . KEY_PATH + "/" + self . KEY_PUBLIC , 'w' ) as iii1i1iiiiIi :
   iii1i1iiiiIi . write ( o0o00OO0 )
   if 7 - 7: II11iiII + o0oo0o + O0
 def decrypt_str ( self , encrypt_text ) :
  if 9 - 9: II111iiii . Ooo00oOo00o - Oo / Ooo00oOo00o
  I11 = self . KEY_PATH + "/" + self . KEY_PUBLIC
  if not os . path . isfile ( I11 ) :
   raise Exception ( "Decrypt key not exist or invalid!" )
   if 66 - 66: i1IIi % i1IIi + oOo0O0Ooo + O0 + ooOO00oOo
  ii111111I1iII = Random . new ( ) . read
  with open ( self . KEY_PATH + "/" + self . KEY_PRIVATE ) as iii1i1iiiiIi :
   o0o = iii1i1iiiiIi . read ( )
   o00 = RSA . importKey ( o0o )
   OooOO000 = Cipher_pkcs1_v1_5 . new ( o00 )
   o0O0o0Oo = OooOO000 . decrypt ( base64 . b64decode ( encrypt_text ) , ii111111I1iII )
   return o0O0o0Oo
   if 97 - 97: oOoO0oo0OOOo + II11iiII / iIii1I11I1II1 / i1I1ii1II1iII
 def encrypt_str ( self , message ) :
  I11 = self . KEY_PATH + "/" + self . KEY_PUBLIC
  if not os . path . isfile ( I11 ) :
   raise Exception ( "Encrypt key not exist or invalid!" )
   if 37 - 37: i1I1ii1II1iII - Oo * iiiiIi11i % i11iIiiIii - o0oo0o
  with open ( I11 ) as iii1i1iiiiIi :
   o0o = iii1i1iiiiIi . read ( )
   o00 = RSA . importKey ( o0o )
   OooOO000 = Cipher_pkcs1_v1_5 . new ( o00 )
   o0oO = base64 . b64encode ( OooOO000 . encrypt ( message ) )
   return o0oO
   if 1 - 1: ooOO00oOo - iiiiIi11i . OoOO0ooOOoo0O . ooOO00oOo / OoO0O00 + OoOO0ooOOoo0O
   if 78 - 78: O0 . iiiiIi11i . II111iiii % II11iiII
   if 49 - 49: o0000oOoOoO0o / ooOO00oOo . II111iiii
   if 68 - 68: i11iIiiIii % oOoO0oo0OOOo + i11iIiiIii
   if 31 - 31: II111iiii . oo
   if 1 - 1: OoO0O00 / Ooo00oOo00o % i1I1ii1II1iII * oooO0oo0oOOOO . i11iIiiIii
   if 2 - 2: oOoO0oo0OOOo * OoOO0ooOOoo0O - iIii1I11I1II1 + oo . iiiiIi11i % i1I1ii1II1iII
   if 92 - 92: i1I1ii1II1iII
   if 25 - 25: OoO0O00 - oo / OoooooooOO / Ooo00oOo00o
   if 12 - 12: oo * i1I1ii1II1iII % i1IIi % iIii1I11I1II1
   if 20 - 20: II11iiII % o0000oOoOoO0o / o0000oOoOoO0o + o0000oOoOoO0o
   if 45 - 45: iiiiIi11i - oooO0oo0oOOOO - OoooooooOO - ooOO00oOo . II111iiii / O0
oo0o00O = "report_"
o00O0OoO = "report_"
i1I = "report_"
if 72 - 72: i1IIi / ooOO00oOo + OoooooooOO - OoO0O00
if 29 - 29: oOoO0oo0OOOo + iiiiIi11i % O0
class I1I11 ( models . Model ) :
 _name = 'cf.cfprint.license'
 _description = u'许可证信息'
 if 34 - 34: oo . II11iiII * oOoO0oo0OOOo + o0oo0o
 mcode = fields . Char ( string = u'机器码' , default = lambda i11111IIIII : ii1I . get_machine_code ( ) , help = u'服务器机器码' )
 license = fields . Binary ( string = u'许可证' , help = u'授权许可证文件，下载后改名为cfprint.lic放到客户端cfprint目录下。' )
 note = fields . Char ( string = u'备注' )
 if 19 - 19: oOo0O0Ooo * i1IIi
 @ api . model
 def create ( self , vals ) :
  vals [ 'mcode' ] = ii111iI1iIi1 = ii1I . get_machine_code ( ) or ''
  return super ( I1I11 , self ) . create ( vals )
  if 78 - 78: ooOO00oOo . II11iiII + ooOO00oOo / OoOO0ooOOoo0O / ooOO00oOo
 @ api . multi
 def write ( self , vals ) :
  vals [ 'mcode' ] = ii111iI1iIi1 = ii1I . get_machine_code ( ) or ''
  return super ( I1I11 , self ) . write ( vals )
  if 54 - 54: oOo0O0Ooo % i1I1ii1II1iII
class IIiII111iiI1I ( models . Model ) :
 _inherit = 'ir.model'
 if 11 - 11: II111iiii * II111iiii % iIii1I11I1II1 * o0oo0o + oOo0O0Ooo / oo
 def name_get ( self ) :
  return [ ( ii1Ii11I . id , '%s(%s)' % ( ii1Ii11I . name , ii1Ii11I . model ) ) for ii1Ii11I in self ]
  if 80 - 80: II111iiii
class O0O ( models . Model ) :
 _name = 'cf.report.define'
 _description = u'报表定义'
 if 1 - 1: II111iiii
 name = fields . Char ( string = u'报表ID' , copy = True , help = u"用一确定报表的唯一ID，只允许英文、数字和下划线。" )
 comment = fields . Char ( string = u'报表中文名称' , copy = True )
 model_id = fields . Many2one ( 'ir.model' , string = u'数据表(model)' , required = True , copy = True , help = u"报表对应的数据表(model)" )
 template_id = fields . Many2one ( 'cf.template' , string = u'报表模板' , copy = True , help = u"该报表使用的打印模板。\n模板如果尚未设计，可以先创建一个模板定义，待生成数据并设计报表模板后再上传到模板库。" )
 company_id = fields . Many2one ( 'res.company' , string = u'所属公司' , default = lambda OOooooO0Oo : OOooooO0Oo . env [ 'res.company' ] . _company_default_get ( '' ) )
 open_print = fields . Boolean ( string = u"是否弹出打印" , default = False )
 use_client_templ = fields . Boolean ( string = u"使用客户端模板" , default = False , help = u"" )
 client_templ_name = fields . Char ( string = u"客户端模板文件名" , help = u"如果设置了使用客户端模板，则在此录入客户端模板路径和文件名" )
 field_ids = fields . One2many ( "cf.report.define.field" , "report_id" , string = u"字段" , help = u"要在报表模板中使用的字段信息" )
 state = fields . Selection ( [ ( 'draft' , u'草稿' ) , ( 'defined' , u'完成报表定义' ) ] , string = u"状态" , default = "draft" )
 note = fields . Text ( string = u"备注" )
 if 91 - 91: Ooo00oOo00o . iIii1I11I1II1 / iiiiIi11i + i1IIi
 _sql_constraints = [
 ( 'uniq_name' , 'unique(name)' , _ ( u'报表名称必须唯一!' ) ) ,
 ]
 if 42 - 42: Oo . Ooo00oOo00o . Oo - oOoO0oo0OOOo
 @ api . model
 def create ( self , vals ) :
  if not vals . get ( "template_id" , False ) :
   i1ii1I1I1 = vals . get ( "name" , False )
   oO = vals . get ( "comment" , False )
   if not i1ii1I1I1 :
    raise ValidationError ( _ ( u"请先指定报表ID！" ) )
   oO0O0o0Oooo = "cf_templ_%s" % ( o00O0OoO , i1ii1I1I1 . replace ( '.' , '_' ) )
   I1Ii1iI1 = self . env [ "cf.template" ] . search ( [ ( 'templ_id' , '=' , oO0O0o0Oooo ) ] , limit = 1 )
   if not I1Ii1iI1 :
    I1Ii1iI1 = self . env [ "cf.template" ] . create ( {
 "templ_id" : oO0O0o0Oooo ,
 "name" : ( oO or oO0O0o0Oooo ) + "打印模板" ,
 "description" : ( oO or oO0O0o0Oooo ) + "打印模板" ,
 } )
   vals [ "template_id" ] = I1Ii1iI1 . id
   if 87 - 87: OoO0O00 . oooO0oo0oOOOO
  return super ( O0O , self ) . create ( vals )
  if 75 - 75: Oo + oOo0O0Ooo + Ooo00oOo00o * OoOO0ooOOoo0O % iiiiIi11i . i1I1ii1II1iII
 @ api . multi
 def unlink ( self ) :
  for oOI1Ii1I1 in self :
   oOI1Ii1I1 . _remove_report ( )
  return super ( O0O , self ) . unlink ( )
  if 28 - 28: O0 * OoO0O00 - II11iiII % iIii1I11I1II1 * o0000oOoOoO0o - i11iIiiIii
 def _get_report_id ( self ) :
  self . ensure_one ( )
  return "%s%s" % ( i1I , self . name )
  if 7 - 7: OoO0O00 + iiiiIi11i - o0oo0o % o0000oOoOoO0o + oOoO0oo0OOOo
 def _get_report_name ( self , with_module = True ) :
  self . ensure_one ( )
  if with_module :
   return "cf_report_designer.%s%s" % ( o00O0OoO , self . name . replace ( '.' , '_' ) )
  else :
   return "%s%s" % ( o00O0OoO , self . name . replace ( '.' , '_' ) )
   if 53 - 53: i1IIi - OoOO0ooOOoo0O . oOo0O0Ooo
 def _get_report_file ( self , with_module = True ) :
  self . ensure_one ( )
  if with_module :
   return "cf_report_designer.%s%s" % ( oo0o00O , self . name . replace ( '.' , '_' ) )
  else :
   return "%s%s" % ( oo0o00O , self . name . replace ( '.' , '_' ) )
   if 39 - 39: II111iiii / Oo + o0oo0o / oOo0O0Ooo
 @ api . one
 def _remove_report ( self ) :
  I1Ii11i = self . _get_report_id ( )
  i1111I1I = self . _get_report_name ( )
  i1i = self . _get_report_file ( )
  if 56 - 56: oOoO0oo0OOOo % O0 - oo
  if 100 - 100: o0000oOoOoO0o - O0 % iiiiIi11i * II11iiII + oo
  self . env [ "ir.model.data" ] . sudo ( ) . search ( [ ( 'name' , '=' , I1Ii11i ) ] ) . unlink ( )
  if 88 - 88: OoooooooOO - ooOO00oOo * O0 * OoooooooOO . OoooooooOO
  I111iI = self . env [ 'ir.actions.report' ] . sudo ( ) . search ( [ ( 'report_name' , '=' , i1111I1I ) ] )
  for oOI1Ii1I1 in I111iI :
   oOI1Ii1I1 . unlink_action ( )
   oOI1Ii1I1 . unlink ( )
   if 56 - 56: oo
   if 54 - 54: o0oo0o / II11iiII . iiiiIi11i % i1I1ii1II1iII
  self . env [ 'ir.ui.view' ] . search ( [ ( 'key' , '=' , i1111I1I ) ] ) . unlink ( )
  if 57 - 57: i11iIiiIii . oOoO0oo0OOOo - o0000oOoOoO0o - iiiiIi11i + oOo0O0Ooo
  if 63 - 63: oOo0O0Ooo * i1I1ii1II1iII
  if 69 - 69: O0 . ooOO00oOo
  if 49 - 49: oo - OoOO0ooOOoo0O
  if 74 - 74: iIii1I11I1II1 * oOoO0oo0OOOo + oOo0O0Ooo / i1IIi / II111iiii . OoO0O00
  if 62 - 62: OoooooooOO * oo
  if 58 - 58: oOo0O0Ooo % Ooo00oOo00o
  if 50 - 50: o0oo0o . Ooo00oOo00o
  if 97 - 97: O0 + oOo0O0Ooo
 def action_retrieve_fields ( self ) :
  if 89 - 89: Ooo00oOo00o + ooOO00oOo * OoOO0ooOOoo0O * o0000oOoOoO0o
  self . env [ "cf.report.define.field" ] . search ( [ ( 'report_id' , '=' , self . id ) ] ) . unlink ( )
  if 37 - 37: OoooooooOO - O0 - Ooo00oOo00o
  if 77 - 77: II11iiII * iIii1I11I1II1
  if 98 - 98: oo % o0000oOoOoO0o * OoooooooOO
  for OoiIIiIi1 in self . model_id . field_id :
   if 74 - 74: i1I1ii1II1iII + Ooo00oOo00o
   oO00O000oO0 = self . env [ 'cf.report.define.field' ] . create ( {
 "report_id" : self . id ,
 "model_id" : OoiIIiIi1 . model_id . id ,
 "field_id" : OoiIIiIi1 . id ,

   } )
   if 79 - 79: OoOO0ooOOoo0O - OoooooooOO - iiiiIi11i - iIii1I11I1II1 * II11iiII
 def action_remove_fields ( self ) :
  self . env [ "cf.report.define.field" ] . search ( [ ( 'report_id' , '=' , self . id ) ] ) . unlink ( )
  if 4 - 4: i11iIiiIii . OoooooooOO / ooOO00oOo % o0oo0o % OoOO0ooOOoo0O * O0
  if 14 - 14: II11iiII / Ooo00oOo00o
 def _make_report_defind ( self ) :
  I1Ii11i = self . _get_report_id ( )
  if 32 - 32: oo * OoO0O00
  i1111I1I = self . _get_report_name ( )
  i1i = self . _get_report_file ( )
  if 78 - 78: II11iiII - OoooooooOO - oOoO0oo0OOOo / Oo / II111iiii
  if 29 - 29: oo % oo
  Oo0O0 = self . env [ 'ir.actions.report' ]
  Ooo0OOoOoO0 = Oo0O0 . create ( {
 "name" : self . comment or self . name ,
 "type" : "ir.actions.report" ,
 "binding_type" : "report" ,
 "model" : self . model_id . model ,
 "report_type" : "qweb-html" ,
 "report_name" : i1111I1I ,
 "report_file" : i1i ,
  "multi" : False ,
 "print_report_name" : self . comment or self . name ,
  "attachment_use" : False ,
 "cf_report_define_id" : self . id ,
 } )
  if Ooo0OOoOoO0 :
   self . env [ "ir.model.data" ] . create ( {
 "name" : "action_%s" % ( I1Ii11i ) ,
 "model" : "ir.actions.report" ,
 "module" : "cf_report_designer" ,
 "noupdate" : False ,
 "res_id" : Ooo0OOoOoO0 . id
 } )
   if 70 - 70: iiiiIi11i
   Ooo0OOoOoO0 . create_action ( )
   if 59 - 59: Ooo00oOo00o % iiiiIi11i
 def _make_templ ( self ) :
  if 6 - 6: iIii1I11I1II1 % i11iIiiIii % oOoO0oo0OOOo
  if 93 - 93: oooO0oo0oOOOO * OoooooooOO + Oo
  IiII111i1i11 = "%s%s" % ( o00O0OoO , self . name . replace ( '.' , '_' ) )
  I1Ii11i = self . _get_report_id ( )
  i1111I1I = self . _get_report_name ( )
  i1i = self . _get_report_file ( )
  if 40 - 40: Oo * oooO0oo0oOOOO * i11iIiiIii
  oo0OO00OoooOo = self . _get_report_name ( False )
  if 19 - 19: oOoO0oo0OOOo % OoooooooOO % oooO0oo0oOOOO * Ooo00oOo00o % O0
  ooo = """<?xml version="1.0"?>
<t t-name="%s">
  <t t-call="cfprint.html_container">
    <t t-raw="show_message"/>
  </t>
<script type="text/javascript">
  <t t-raw="cfprint_json"/>
</script>
</t>
""" % ( oo0OO00OoooOo )
  if 27 - 27: Oo % oo
  o0oooOO00 = self . env [ 'ir.ui.view' ]
  if 32 - 32: o0oo0o
  try :
   Iii1 = o0oooOO00 . create ( {
 "name" : I1Ii11i ,
 "key" : i1111I1I ,
 "priority" : 16 ,
 "type" : "qweb" ,
 "arch_db" : ooo ,
 "mode" : "primary" ,
 "active" : True ,

   } )
   if Iii1 :
    self . env [ "ir.model.data" ] . create ( {
 "name" : oo0OO00OoooOo ,
 "model" : "ir.ui.view" ,
 "module" : "cf_report_designer" ,
 "noupdate" : False ,
 "res_id" : Iii1 . id
 } )
    if 61 - 61: oOo0O0Ooo - II11iiII - i1IIi
  except Exception as IiI1iIiIIIii :
   IiII1IiiIiI1 . error ( "Create report template[%s] failed." % ( i1111I1I ) )
   raise IiI1iIiIIIii
   if 53 - 53: i1IIi
 def action_generate ( self ) :
  if 59 - 59: Ooo00oOo00o
  if 81 - 81: oOo0O0Ooo - oOo0O0Ooo . i1I1ii1II1iII
  if 73 - 73: OoOO0ooOOoo0O % i11iIiiIii - oo
  self . _remove_report ( )
  if 7 - 7: O0 * i11iIiiIii * o0000oOoOoO0o + Oo % ooOO00oOo - Oo
  if 39 - 39: OoO0O00 * II11iiII % II11iiII - OoooooooOO + Ooo00oOo00o - OoOO0ooOOoo0O
  self . _make_report_defind ( )
  if 23 - 23: i11iIiiIii
  if 30 - 30: Ooo00oOo00o - i1IIi % II111iiii + OoOO0ooOOoo0O * iIii1I11I1II1
  self . _make_templ ( )
  if 81 - 81: oooO0oo0oOOOO % i1IIi . iIii1I11I1II1
  self . write ( { "state" : "defined" } )
  if 4 - 4: i11iIiiIii % ooOO00oOo % i1IIi / oooO0oo0oOOOO
 def action_design ( self ) :
  if 6 - 6: i1I1ii1II1iII / oo % II11iiII - oo
  if 31 - 31: II11iiII
  if 23 - 23: o0oo0o . oooO0oo0oOOOO
  OO0000o = self . env [ self . model_id . model ] . search ( [ ] , limit = 5 )
  i1I1i1 = [ i11111IIIII . id for i11111IIIII in OO0000o ]
  if 81 - 81: Oo - iIii1I11I1II1 - i1IIi / o0oo0o - O0 * OoOO0ooOOoo0O
  if 20 - 20: iiiiIi11i % oooO0oo0oOOOO
  I1Ii11i = "cf_report_designer.%s%s" % ( i1I , self . name )
  if 19 - 19: oOoO0oo0OOOo % oooO0oo0oOOOO + Oo / o0oo0o . Oo
  i1111I1I = "cf_report_designer.%s%s" % ( o00O0OoO , self . name )
  IiIi1I1 = { "is_design" : True ,
 "docs" : OO0000o ,
 "docids" : i1I1i1
 }
  if 39 - 39: II111iiii + oOo0O0Ooo - Oo . oOo0O0Ooo
  return ( self . env [ 'ir.actions.report' ] . search ( [ ( 'report_name' , '=' , i1111I1I ) ] , limit = 1 )
 . with_context ( { 'is_design' : True } )
 . report_action ( i1I1i1 , data = IiIi1I1 ) )
  if 84 - 84: ooOO00oOo + i1IIi - II111iiii . oOoO0oo0OOOo * OoooooooOO + oo
  if 38 - 38: II11iiII + II111iiii % Oo % oOo0O0Ooo - o0000oOoOoO0o / OoooooooOO
class oOOoo0000O0o0 ( models . Model ) :
 _name = 'cf.report.define.field'
 _description = u'报表字段'
 _order = 'report_id, id'
 if 1 - 1: iiiiIi11i + iiiiIi11i % oOo0O0Ooo + i11iIiiIii
 report_id = fields . Many2one ( "cf.report.define" , string = u"报表定义" , required = True , ondelete = 'cascade' , help = u"字段所在的报表定义" )
 model_id = fields . Many2one ( 'ir.model' , string = u"数据表(模型)" , required = True , ondelete = 'cascade' , help = u"字段所在的model" )
 model_name = fields . Char ( related = "model_id.name" , string = u"模型名称" )
 field_id = fields . Many2one ( "ir.model.fields" , string = u"字段" , required = True , ondelete = 'cascade' )
 name = fields . Char ( related = "field_id.name" , string = u'字段名称' )
 field_description = fields . Char ( related = "field_id.field_description" , string = u'字段说明' )
 ttype = fields . Selection ( related = "field_id.ttype" , string = u'字段类型' )
 related_field_id = fields . Many2one ( "cf.report.define.field" , string = u"关联字段" , help = u"与关联表关联的字段(related_external_field_ids)" , oldname = "parent_field_id" )
 related_external_field_ids = fields . One2many ( "cf.report.define.field" , "related_field_id" , string = u"关联数据表字段" , help = u"与当前表相关联的表字段" , oldname = "sub_field_ids" )
 note = fields . Text ( string = u"备注" )
 if 56 - 56: Ooo00oOo00o
 related_field_model_id = fields . Many2one ( 'ir.model' , compute = "_compute_relation_model" , string = u"关联数据表（模型）" , help = u"关联字段所在的model。当前字段为One2many，Many2many，Many2one时有值。" )
 related_field_model_name = fields . Char ( related = "related_field_model_id.name" , string = u"关联数据表名称" , help = u"关联字段所在的model名称" )
 if 28 - 28: i1I1ii1II1iII . i1I1ii1II1iII % iIii1I11I1II1 * iIii1I11I1II1 . Ooo00oOo00o / i1I1ii1II1iII
 _sql_constraints = [
 ( 'uniq_repoer_model_field' , 'unique(report_id, model_id, related_field_id, field_id)' , u'报表 + 表 + 关联上级字段 + 字段必须唯一!' ) ,
 ]
 if 27 - 27: ooOO00oOo + Oo - i1IIi
 @ api . model
 def create ( self , vals ) :
  if 69 - 69: oooO0oo0oOOOO - O0 % oOoO0oo0OOOo + i11iIiiIii . oOo0O0Ooo / ooOO00oOo
  if not vals . get ( "model_id" , False ) :
   oO00O000oO0 = self . env [ "ir.model.fields" ] . browse ( vals . get ( "field_id" , 0 ) )
   if oO00O000oO0 :
    vals [ "model_id" ] = oO00O000oO0 . model_id . id
    if 79 - 79: O0 * i11iIiiIii - oooO0oo0oOOOO / oooO0oo0oOOOO
    if 48 - 48: O0
  self . search ( [ ( 'report_id' , '=' , vals . get ( "report_id" , 0 ) ) , ( 'model_id' , '=' , vals . get ( "model_id" , 0 ) ) ,
 ( 'related_field_id' , '=' , vals . get ( "related_field_id" , 0 ) ) , ( 'field_id' , '=' , vals . get ( "field_id" , 0 ) ) ] ) . unlink ( )
  if 93 - 93: i11iIiiIii - oo * oOoO0oo0OOOo * OoOO0ooOOoo0O % O0 + OoooooooOO
  return super ( oOOoo0000O0o0 , self ) . create ( vals )
  if 25 - 25: oooO0oo0oOOOO + o0000oOoOoO0o / Oo . Ooo00oOo00o % O0 * ooOO00oOo
  if 84 - 84: Oo % o0000oOoOoO0o + i11iIiiIii
 def _compute_relation_model ( self ) :
  for oO00O000oO0 in self :
   II1I1Ii = self . env [ 'ir.model' ] . _get ( oO00O000oO0 . field_id . relation )
   oO00O000oO0 . related_field_model_id = II1I1Ii . id if II1I1Ii else None
   if 62 - 62: O0 % OoOO0ooOOoo0O . OoOO0ooOOoo0O - iIii1I11I1II1 / i11iIiiIii
 def action_retrieve_fields ( self ) :
  if self . field_id and ( self . field_id . ttype == 'one2many' or self . field_id . ttype == 'many2many' or self . field_id . ttype == 'many2one' ) :
   if 31 - 31: iIii1I11I1II1 / ooOO00oOo / oOoO0oo0OOOo
   if self . env . get ( self . field_id . relation , '_EMPTY' ) == '_EMPTY' :
    raise AccessError ( _ ( u"未找到关联字段对应的表（%s），无法获取关联表字段！" % ( self . field_id . relation ) ) )
    if 41 - 41: OoO0O00
    if 10 - 10: OoO0O00 / OoO0O00 / o0oo0o . o0oo0o
   OOoo = self . env [ 'ir.model' ] . _get ( self . field_id . relation )
   if 50 - 50: ooOO00oOo
   if 43 - 43: II111iiii . iiiiIi11i / oOoO0oo0OOOo
   self . action_remove_fields ( )
   if 20 - 20: oo
   if 95 - 95: i1I1ii1II1iII - oo
   for OoiIIiIi1 in OOoo . field_id :
    oO00O000oO0 = self . env [ 'cf.report.define.field' ] . create ( {
 "related_field_id" : self . id ,
 "report_id" : self . report_id . id ,
 "model_id" : OoiIIiIi1 . model_id . id ,
 "field_id" : OoiIIiIi1 . id ,
 } )
    if 34 - 34: Oo * oo . i1IIi * Oo / Oo
 def action_remove_fields ( self ) :
  if self . field_id and ( self . field_id . ttype == 'one2many' or self . field_id . ttype == 'many2many' or self . field_id . ttype == 'many2one' ) :
   if 30 - 30: oOoO0oo0OOOo + OoO0O00 / OoO0O00 % oOoO0oo0OOOo . oOoO0oo0OOOo
   OOoo = self . env [ 'ir.model' ] . _get ( self . field_id . relation )
   if 55 - 55: Oo - OoOO0ooOOoo0O + II111iiii + i1I1ii1II1iII % o0000oOoOoO0o
   if 41 - 41: i1IIi - OoOO0ooOOoo0O - o0000oOoOoO0o
   self . env [ "cf.report.define.field" ] . search ( [ ( 'report_id' , '=' , self . report_id . id ) , ( 'model_id' , '=' , OOoo . id ) , ( 'related_field_id' , '=' , self . id ) ] ) . unlink ( )
   if 8 - 8: ooOO00oOo + o0oo0o - Ooo00oOo00o % OoO0O00 % Ooo00oOo00o * iiiiIi11i
 def action_view_sub_fields ( self ) :
  self . ensure_one ( )
  if 9 - 9: OoO0O00 - i11iIiiIii - II11iiII * o0000oOoOoO0o + Oo
  iIIII = self . env . ref ( 'cf_report_designer.cf_report_define_field_form' ) . id
  return { 'type' : 'ir.actions.act_window' ,
 'res_model' : 'cf.report.define.field' ,
 'view_mode' : 'form' ,
 'views' : [ ( iIIII , 'form' ) ] ,
 'res_id' : self . id ,
 'target' : 'new' ,
 'limit' : 1000 ,
 'name' : u'关联表字段' ,
 'flags' : { 'form' : { 'action_buttons' : False } }
 }
  if 45 - 45: oOoO0oo0OOOo % oo - i11iIiiIii
  if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * oo
  if 46 - 46: oOo0O0Ooo + ooOO00oOo
  if 70 - 70: i1I1ii1II1iII / iIii1I11I1II1
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / oOoO0oo0OOOo
  if 96 - 96: OoooooooOO + iiiiIi11i
  if 44 - 44: iiiiIi11i
from xml . dom import minidom
import uuid
if 20 - 20: OoOO0ooOOoo0O + o0000oOoOoO0o / O0 % iIii1I11I1II1
oOo0O = "<h5 style=\"margin-top: 3rem; text-align: center;\">%s</h4>"
if 64 - 64: oOoO0oo0OOOo - i1I1ii1II1iII + i1I1ii1II1iII - OoOO0ooOOoo0O
if 30 - 30: iIii1I11I1II1 . oo . II11iiII / Ooo00oOo00o
class iiI1I1 ( models . Model ) :
 if 56 - 56: oo . O0 + OoO0O00
 _inherit = 'ir.actions.report'
 if 1 - 1: i1I1ii1II1iII
 if 97 - 97: II11iiII + i1I1ii1II1iII + O0 + i11iIiiIii
 if 77 - 77: Ooo00oOo00o / OoooooooOO
 _description = 'Report Action'
 if 46 - 46: Ooo00oOo00o % iIii1I11I1II1 . i1I1ii1II1iII % i1I1ii1II1iII + i11iIiiIii
 cf_report_define_id = fields . Many2one ( "cf.report.define" , string = u"报表定义" , help = u"如果是康虎云报表，则保存对应的报表定义。" )
 if 72 - 72: iIii1I11I1II1 * o0000oOoOoO0o % Oo / ooOO00oOo
 def _make_cfprint_json ( self , values ) :
  if 35 - 35: Oo + i1IIi % oOoO0oo0OOOo % OoOO0ooOOoo0O + iiiiIi11i
  if 17 - 17: i1IIi
  def iiIi1i ( lst ) :
   I1i11111i1i11 = set ( )
   if 77 - 77: oOoO0oo0OOOo + ooOO00oOo / iiiiIi11i + O0 * Ooo00oOo00o
   if 28 - 28: Oo + i11iIiiIii / OoOO0ooOOoo0O % oOo0O0Ooo % OoO0O00 - O0
   if 54 - 54: i1IIi + II111iiii
   if 83 - 83: oOoO0oo0OOOo - oo + II11iiII
   if 5 - 5: o0000oOoOoO0o
   iIi1i1iIi1iI = [ ]
   for iiIi1iI1iIii in lst :
    o00OooO0oo = tuple ( iiIi1iI1iIii . items ( ) )
    if o00OooO0oo not in I1i11111i1i11 :
     I1i11111i1i11 . add ( o00OooO0oo )
     iIi1i1iIi1iI . append ( iiIi1iI1iIii )
   return iIi1i1iIi1iI
   if 89 - 89: o0000oOoOoO0o
  def ooOoOO0OoO00o ( field ) :
   II1iiiiII = "str"
   if 61 - 61: i1I1ii1II1iII % oo - Ooo00oOo00o - II111iiii % O0
   if 90 - 90: iIii1I11I1II1 + oOoO0oo0OOOo + Oo - o0oo0o * oooO0oo0oOOOO . oOoO0oo0OOOo
   if 37 - 37: Oo % i11iIiiIii % II111iiii . O0 . o0000oOoOoO0o
   if 51 - 51: ooOO00oOo - O0 % iiiiIi11i - II111iiii
   if 31 - 31: i1I1ii1II1iII / OoO0O00 - i1I1ii1II1iII - II11iiII
   if field . ttype in [ "binary" ] :
    II1iiiiII = "blob"
   elif field . ttype in [ "boolean" ] :
    II1iiiiII = "boolean"
   elif field . ttype in [ 'char' , 'text' , 'html' , 'selection' , 'reference' ] :
    II1iiiiII = "str"
   elif field . ttype in [ 'date' , 'datetime' ] :
    II1iiiiII = "date"
   elif field . ttype in [ 'float' , 'monetary' ] :
    II1iiiiII = "float"
   elif field . ttype in [ "integer" ] :
    II1iiiiII = "int"
   elif field . ttype in [ "many2one" ] :
    II1iiiiII = "int"
   return II1iiiiII
   if 7 - 7: i1I1ii1II1iII % O0 . oOo0O0Ooo + oo - OoOO0ooOOoo0O
  def o0o0O00oo0 ( report_define , model , fields , docs , datas , related_field = False ) :
   Ii1ii1IiIII = { }
   if 57 - 57: iIii1I11I1II1 / OoOO0ooOOoo0O - i1IIi
   if 51 - 51: oooO0oo0oOOOO
   if 25 - 25: OoooooooOO + oooO0oo0oOOOO * oOoO0oo0OOOo
   if 92 - 92: oo + OoOO0ooOOoo0O + O0 / Ooo00oOo00o + o0oo0o
   if 18 - 18: Oo * oOo0O0Ooo . i1I1ii1II1iII / oOoO0oo0OOOo / i11iIiiIii
   if 21 - 21: iiiiIi11i / oOoO0oo0OOOo + o0000oOoOoO0o + OoooooooOO
   if 91 - 91: i11iIiiIii / i1IIi + i1I1ii1II1iII + Oo * i11iIiiIii
   if 66 - 66: iIii1I11I1II1 % i1IIi - O0 + OoOO0ooOOoo0O * o0oo0o . oooO0oo0oOOOO
   if 52 - 52: Oo + O0 . i1I1ii1II1iII . oOoO0oo0OOOo . ooOO00oOo
   if 97 - 97: oo / i1I1ii1II1iII
   if 71 - 71: II111iiii / i1IIi . oOoO0oo0OOOo % OoooooooOO . oOo0O0Ooo
   Iiiiii111i1ii = model . model . replace ( "." , "_" )
   if 25 - 25: II11iiII - Oo / i11iIiiIii
   if 41 - 41: i1IIi % i1I1ii1II1iII + iIii1I11I1II1
   if 2 - 2: iIii1I11I1II1 * OoO0O00 % iiiiIi11i - II111iiii - i1I1ii1II1iII
   if 3 - 3: o0oo0o
   if 45 - 45: o0oo0o
   if 83 - 83: oOo0O0Ooo . OoooooooOO
   if not datas . get ( Iiiiii111i1ii , False ) :
    datas [ Iiiiii111i1ii ] = { "cols" : [ ] , "rows" : [ ] }
    if 58 - 58: i11iIiiIii + OoooooooOO % OoooooooOO / oooO0oo0oOOOO / i11iIiiIii
   oOOoo = datas [ Iiiiii111i1ii ] [ "cols" ]
   if 14 - 14: Ooo00oOo00o * iiiiIi11i
   if 81 - 81: o0000oOoOoO0o * Ooo00oOo00o + o0oo0o + OoO0O00 - OoooooooOO
   if 32 - 32: o0000oOoOoO0o * O0
   if 100 - 100: Oo % iIii1I11I1II1 * II111iiii - i1I1ii1II1iII
   if 92 - 92: Oo
   if 22 - 22: OoO0O00 % i1I1ii1II1iII * oOoO0oo0OOOo / II11iiII % i11iIiiIii * OoOO0ooOOoo0O
   if 95 - 95: OoooooooOO - oooO0oo0oOOOO * oo + oOo0O0Ooo
   if 10 - 10: Ooo00oOo00o / i11iIiiIii
   if 92 - 92: OoOO0ooOOoo0O . o0oo0o
   if 85 - 85: oOoO0oo0OOOo . o0oo0o
   if 78 - 78: Oo * o0oo0o + iIii1I11I1II1 + iIii1I11I1II1 / o0oo0o . o0000oOoOoO0o
   if 97 - 97: Oo / o0oo0o % i1IIi % oOoO0oo0OOOo
   if 18 - 18: iIii1I11I1II1 % OoOO0ooOOoo0O
   if 95 - 95: Oo + i11iIiiIii * o0oo0o - i1IIi * o0oo0o - iIii1I11I1II1
   if 75 - 75: OoooooooOO * oooO0oo0oOOOO
   if 9 - 9: oooO0oo0oOOOO - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
   if 39 - 39: oooO0oo0oOOOO * OoO0O00 + iIii1I11I1II1 - oooO0oo0oOOOO + II11iiII
   if 69 - 69: O0
   if 85 - 85: Oo / O0
   if 18 - 18: Ooo00oOo00o % O0 * oOoO0oo0OOOo
   if 62 - 62: o0oo0o . oooO0oo0oOOOO . OoooooooOO
   if 11 - 11: II11iiII / OoOO0ooOOoo0O
   if 73 - 73: i1IIi / i11iIiiIii
   if 58 - 58: OoO0O00 . II111iiii + iiiiIi11i - i11iIiiIii / II111iiii / O0
   if 85 - 85: oOo0O0Ooo + II11iiII
   if 10 - 10: oooO0oo0oOOOO / ooOO00oOo + oOo0O0Ooo / i1IIi
   if 27 - 27: o0000oOoOoO0o
   if 67 - 67: oo
   if 55 - 55: oOoO0oo0OOOo - i1I1ii1II1iII * Ooo00oOo00o + oOo0O0Ooo * oOo0O0Ooo * O0
   if 91 - 91: o0oo0o - II11iiII % iIii1I11I1II1 - OoooooooOO % Oo
   if 98 - 98: ooOO00oOo . ooOO00oOo * iiiiIi11i * II111iiii * o0oo0o
   if 92 - 92: OoO0O00
   if 40 - 40: oOo0O0Ooo / oooO0oo0oOOOO
   if 79 - 79: ooOO00oOo - iIii1I11I1II1 + o0000oOoOoO0o - o0oo0o
   if 93 - 93: II111iiii . oo - OoO0O00 + oOo0O0Ooo
   if 61 - 61: II111iiii
   if 15 - 15: i11iIiiIii % oo * OoOO0ooOOoo0O / o0oo0o
   if 90 - 90: i1I1ii1II1iII
   if 31 - 31: II11iiII + O0
   if 87 - 87: Oo
   if 45 - 45: ooOO00oOo / OoooooooOO - i1I1ii1II1iII / o0000oOoOoO0o % oooO0oo0oOOOO
   if 83 - 83: oo . iIii1I11I1II1 - oooO0oo0oOOOO * i11iIiiIii
   if 20 - 20: i1IIi * o0oo0o + II111iiii % Ooo00oOo00o % iiiiIi11i
   if 13 - 13: OoO0O00
   if 60 - 60: oOoO0oo0OOOo * oo
   if 17 - 17: II11iiII % OoO0O00 / oOoO0oo0OOOo . oooO0oo0oOOOO * II11iiII - II111iiii
   if 41 - 41: o0000oOoOoO0o
   if 77 - 77: o0oo0o
   if 65 - 65: II111iiii . oo % iiiiIi11i * ooOO00oOo
   if 38 - 38: oOo0O0Ooo / i1I1ii1II1iII % OoO0O00
   if 11 - 11: i1I1ii1II1iII - iiiiIi11i + II111iiii - iIii1I11I1II1
   if 7 - 7: oooO0oo0oOOOO - OoOO0ooOOoo0O / II111iiii * o0000oOoOoO0o . i1I1ii1II1iII * i1I1ii1II1iII
   if 61 - 61: OoOO0ooOOoo0O % Oo - ooOO00oOo / OoO0O00
   if 4 - 4: OoooooooOO - i1IIi % o0000oOoOoO0o - II11iiII * Ooo00oOo00o
   if 85 - 85: OoooooooOO * iIii1I11I1II1 . i1I1ii1II1iII / OoooooooOO % oo % O0
   if 36 - 36: o0000oOoOoO0o / II111iiii / oooO0oo0oOOOO / oooO0oo0oOOOO + oOoO0oo0OOOo
   if 95 - 95: oooO0oo0oOOOO
   if 51 - 51: II111iiii + oooO0oo0oOOOO . i1IIi . oOoO0oo0OOOo + oOo0O0Ooo * oo
   if 72 - 72: iiiiIi11i + iiiiIi11i / II111iiii . OoooooooOO % o0000oOoOoO0o
   if 49 - 49: iiiiIi11i . ooOO00oOo - OoO0O00 * OoooooooOO . OoO0O00
   if 2 - 2: OoooooooOO % II11iiII
   if 63 - 63: oo % iIii1I11I1II1
   if 39 - 39: i1I1ii1II1iII / II111iiii / oOoO0oo0OOOo % oo
   for O0Oo00 in docs :
    ii1IiIIi1i = { }
    for oO00O000oO0 in [ iiIi1iI1iIii for iiIi1iI1iIii in fields if iiIi1iI1iIii . model_id . model == model . model ] :
     try :
      if oO00O000oO0 . ttype == 'binary' :
       ii1IiIIi1i [ oO00O000oO0 . name ] = "base64/jpg:%s" % ( O0Oo00 [ oO00O000oO0 . name ] . strip ( ) . decode ( "UTF-8" ) . replace ( "\n" , "" ) if O0Oo00 [ oO00O000oO0 . name ] else "" )
       if 54 - 54: Oo
      elif oO00O000oO0 . ttype in [ 'boolean' ] :
       ii1IiIIi1i [ oO00O000oO0 . name ] = O0Oo00 [ oO00O000oO0 . name ]
       if 67 - 67: II11iiII . OoO0O00 + oOo0O0Ooo - OoooooooOO
      elif oO00O000oO0 . ttype in [ 'char' , 'text' , 'html' , 'selection' , 'reference' ] :
       ii1IiIIi1i [ oO00O000oO0 . name ] = O0Oo00 [ oO00O000oO0 . name ] if O0Oo00 [ oO00O000oO0 . name ] else ""
       if 70 - 70: II11iiII / II111iiii - iIii1I11I1II1 - i1I1ii1II1iII
       if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - OoOO0ooOOoo0O
       if oO00O000oO0 . ttype == 'char' and O0Oo00 [ oO00O000oO0 . name ] and len ( O0Oo00 [ oO00O000oO0 . name ] ) > Ii1ii1IiIII . get ( oO00O000oO0 . name , 0 ) :
        Ii1ii1IiIII [ oO00O000oO0 . name ] = len ( O0Oo00 [ oO00O000oO0 . name ] )
        if 30 - 30: oOo0O0Ooo
      elif oO00O000oO0 . ttype in [ 'date' , 'datetime' ] :
       ii1IiIIi1i [ oO00O000oO0 . name ] = O0Oo00 [ oO00O000oO0 . name ] . strftime ( "%Y-%m-%d %H:%M:%S" ) if O0Oo00 [ oO00O000oO0 . name ] else ""
       if 21 - 21: i11iIiiIii / o0oo0o % II11iiII * O0 . OoOO0ooOOoo0O - iIii1I11I1II1
      elif oO00O000oO0 . ttype in [ 'float' , 'integer' , 'monetary' ] :
       ii1IiIIi1i [ oO00O000oO0 . name ] = O0Oo00 [ oO00O000oO0 . name ] if O0Oo00 [ oO00O000oO0 . name ] != None else ""
       if 26 - 26: II111iiii * oOo0O0Ooo
      elif oO00O000oO0 . ttype in [ "one2many" , "many2many" ] and len ( oO00O000oO0 . related_external_field_ids ) > 0 :
       ii = O0Oo00 [ oO00O000oO0 . name ]
       oo0o0OoOOO = oO00O000oO0 . related_external_field_ids
       ooO0oO00O0o = self . env [ 'ir.model' ] . _get ( oO00O000oO0 . field_id . relation )
       if ii and len ( ii ) > 0 and oo0o0OoOOO and len ( oo0o0OoOOO ) > 0 and ooO0oO00O0o :
        o0o0O00oo0 ( report_define , ooO0oO00O0o , oo0o0OoOOO , ii , datas )
        if 70 - 70: o0oo0o
      elif oO00O000oO0 . ttype in [ 'many2one' ] :
       ii1IiIIi1i [ oO00O000oO0 . name ] = O0Oo00 [ oO00O000oO0 . name ] . id if O0Oo00 [ oO00O000oO0 . name ] else ""
       ii1IiIIi1i [ oO00O000oO0 . name + "_name" ] = O0Oo00 [ oO00O000oO0 . name ] . name if O0Oo00 [ oO00O000oO0 . name ] and O0Oo00 [ oO00O000oO0 . name ] . name else ""
       ii1IiIIi1i [ oO00O000oO0 . name + "_display_name" ] = O0Oo00 [ oO00O000oO0 . name ] . display_name if O0Oo00 [ oO00O000oO0 . name ] and O0Oo00 [ oO00O000oO0 . name ] . display_name else ""
       if len ( ii1IiIIi1i [ oO00O000oO0 . name + "_name" ] ) > Ii1ii1IiIII . get ( oO00O000oO0 . name + "_name" , 0 ) : Ii1ii1IiIII [ oO00O000oO0 . name + "_name" ] = len ( ii1IiIIi1i [ oO00O000oO0 . name + "_name" ] )
       if len ( ii1IiIIi1i [ oO00O000oO0 . name + "_display_name" ] ) > Ii1ii1IiIII . get ( oO00O000oO0 . name + "_display_name" , 0 ) : Ii1ii1IiIII [ oO00O000oO0 . name + "_display_name" ] = len ( ii1IiIIi1i [ oO00O000oO0 . name + "_display_name" ] )
       if 16 - 16: i1I1ii1II1iII - OoooooooOO % OoO0O00
       if 36 - 36: II11iiII
       if len ( oO00O000oO0 . related_external_field_ids ) > 0 :
        ii = O0Oo00 [ oO00O000oO0 . name ]
        oo0o0OoOOO = oO00O000oO0 . related_external_field_ids
        ooO0oO00O0o = self . env [ 'ir.model' ] . _get ( oO00O000oO0 . field_id . relation )
        if ii and len ( ii ) > 0 and oo0o0OoOOO and len ( oo0o0OoOOO ) > 0 and ooO0oO00O0o :
         o0o0O00oo0 ( report_define , ooO0oO00O0o , oo0o0OoOOO , ii , datas , oO00O000oO0 )
         if 84 - 84: o0oo0o . ooOO00oOo . II111iiii . OoOO0ooOOoo0O / o0000oOoOoO0o % oOoO0oo0OOOo
         if 57 - 57: oo % OoOO0ooOOoo0O - II11iiII . oo / OoO0O00 % i1I1ii1II1iII
         if 56 - 56: iiiiIi11i . i1I1ii1II1iII . oooO0oo0oOOOO * oOo0O0Ooo . Oo / O0
         if 23 - 23: i1IIi + i1I1ii1II1iII + oooO0oo0oOOOO + ooOO00oOo
         if 12 - 12: iIii1I11I1II1 - oOoO0oo0OOOo + i11iIiiIii
         if 10 - 10: oo - i1IIi - Oo % OoO0O00
         if 6 - 6: oOoO0oo0OOOo + iiiiIi11i
         if 48 - 48: iIii1I11I1II1 % i1IIi % i1I1ii1II1iII + Oo
         if 30 - 30: i11iIiiIii % iIii1I11I1II1 . OoOO0ooOOoo0O % iIii1I11I1II1
         if 62 - 62: OoO0O00 * oOo0O0Ooo
     except Exception as OO0 :
      IiII1IiiIiI1 . error ( _ ( u"生成康虎云报表打印数据出错。model: %s, field: %s, Error: %s" ) % ( model . model , oO00O000oO0 . name , OO0 ) )
      pass
      if 84 - 84: oOo0O0Ooo % Oo - oOo0O0Ooo . Ooo00oOo00o
    if ii1IiIIi1i :
     datas [ Iiiiii111i1ii ] [ "rows" ] . append ( ii1IiIIi1i )
     if 5 - 5: oOo0O0Ooo * o0oo0o - oOoO0oo0OOOo / iIii1I11I1II1 % iiiiIi11i + oooO0oo0oOOOO
     if 51 - 51: o0oo0o * II111iiii % Oo
   for oO00O000oO0 in [ iiIi1iI1iIii for iiIi1iI1iIii in fields if iiIi1iI1iIii . model_id . model == model . model ] :
    II1iiiiII = ooOoOO0OoO00o ( oO00O000oO0 )
    if 98 - 98: ooOO00oOo . OoOO0ooOOoo0O % II111iiii
    O0OoOoO00O = Ii1ii1IiIII . get ( oO00O000oO0 . name , 20 ) if II1iiiiII == "str" else 0
    if 96 - 96: oo % OoO0O00 . oOoO0oo0OOOo + II11iiII
    datas [ Iiiiii111i1ii ] [ "cols" ] . append ( { "type" : II1iiiiII , "size" : O0OoOoO00O , "name" : oO00O000oO0 . name , "required" : False , "comment" : oO00O000oO0 . field_description } )
    if 42 - 42: II111iiii * i1I1ii1II1iII * i11iIiiIii - II11iiII . OoooooooOO
    if 76 - 76: II111iiii
    if oO00O000oO0 . ttype in [ "many2one" ] :
     datas [ Iiiiii111i1ii ] [ "cols" ] . append ( { "type" : "str" , "size" : Ii1ii1IiIII . get ( oO00O000oO0 . name + "_name" , 20 ) , "name" : oO00O000oO0 . name + "_name" , "required" : False , "comment" : oO00O000oO0 . field_description } )
     if 26 - 26: II111iiii % i11iIiiIii % iIii1I11I1II1 % OoOO0ooOOoo0O * OoOO0ooOOoo0O * oOoO0oo0OOOo
    if oO00O000oO0 . ttype in [ "many2one" ] :
     datas [ Iiiiii111i1ii ] [ "cols" ] . append ( { "type" : "str" , "size" : Ii1ii1IiIII . get ( oO00O000oO0 . name + "_name" , 20 ) , "name" : oO00O000oO0 . name + "_name" , "required" : False , "comment" : oO00O000oO0 . field_description } )
     datas [ Iiiiii111i1ii ] [ "cols" ] . append ( { "type" : "str" , "size" : Ii1ii1IiIII . get ( oO00O000oO0 . name + "_display_name" , 20 ) , "name" : oO00O000oO0 . name + "_display_name" , "required" : False , "comment" : oO00O000oO0 . field_description } )
     if 24 - 24: II111iiii % o0oo0o - Oo + oo * oOoO0oo0OOOo
     if 2 - 2: o0000oOoOoO0o - oooO0oo0oOOOO
     if 83 - 83: iiiiIi11i % Ooo00oOo00o % o0000oOoOoO0o - II111iiii * II11iiII / OoooooooOO
     if 18 - 18: ooOO00oOo + iIii1I11I1II1 - II111iiii - oo
     if 71 - 71: OoooooooOO
     if 33 - 33: o0oo0o
     if 62 - 62: oOoO0oo0OOOo + o0000oOoOoO0o + i1IIi / OoooooooOO
   datas [ Iiiiii111i1ii ] [ "cols" ] = iiIi1i ( datas [ Iiiiii111i1ii ] [ "cols" ] )
   return datas
   if 7 - 7: Ooo00oOo00o + i1IIi . oo / OoO0O00
   if 22 - 22: Oo - Oo % II11iiII . o0oo0o + iiiiIi11i
   if 63 - 63: oo % o0oo0o * Ooo00oOo00o + o0oo0o / OoO0O00 % i1I1ii1II1iII
  iiI1i1Iii111 = values . get ( "report_define" )
  ii111iI1iIi1 = ii1I . get_machine_code ( ) or ''
  i111I11i = {
 "template" : "" ,
 "ver" : 4 ,
 "Copies" : 1 ,
 "Duplex" : 0 ,
 "mcode" : ii111iI1iIi1 ,
 "Tables" : [ ]
 }
  if 46 - 46: O0 . o0000oOoOoO0o
  OoOO = self . _context . get ( "is_design" , False )
  if OoOO :
   i111I11i [ "design" ] = True
   iIII1I1i1i = oOo0O % ( _ ( u"""请在康虎云报表设计器设计报表。<br/>
            如果报表设计器未打开，请检查康虎云报表是否已启动！<br/><br/><br/>
            模板设计完成后，请在odoo菜单“康虎云报表”--&gt;“模板”菜单中，打开模板记录上传或更新模板！<br/><br/>
            <a href=\"cfprint://open\">启动康虎云报表</a>
            """ ) )
   values . update ( show_message = iIII1I1i1i )
   if 79 - 79: o0000oOoOoO0o . ooOO00oOo
  if iiI1i1Iii111 . use_client_templ and iiI1i1Iii111 . client_templ_name :
   i111I11i [ "template" ] = iiI1i1Iii111 . client_templ_name
  else :
   if not iiI1i1Iii111 . template_id or not iiI1i1Iii111 . template_id . templ_id :
    values . update ( show_message = oOo0O % ( _ ( u"未指定要打印的报表模板，请先指定报表模板。" ) ) )
   IIiI1I1 = self . env [ 'cf.template' ] . search ( [ ( 'templ_id' , '=' , iiI1i1Iii111 . template_id . templ_id ) ] , limit = 1 ) . template
   if not IIiI1I1 or IIiI1I1 == "" :
    if not OoOO :
     values . update ( show_message = oOo0O % ( _ ( u"指定的报表模板未定义或模板无内容，请先设计模板并更新到模板记录表。</h3>" ) ) )
    else :
     i111I11i [ "template" ] = "cf_templ_%s" % ( iiI1i1Iii111 . name . replace ( '.' , '_' ) )
   else :
    i111I11i [ "template" ] = "base64:" + IIiI1I1 . strip ( ) . decode ( "UTF-8" ) . replace ( "\n" , "" )
    if 15 - 15: o0000oOoOoO0o * OoO0O00 % oOoO0oo0OOOo * iIii1I11I1II1 - i11iIiiIii
  OO0000o = values . get ( "docs" )
  if not OO0000o or len ( OO0000o ) < 1 :
   Oo00OOOOoo0oo = self . _context . get ( "active_ids" , [ ] )
   OO0000o = self . env [ iiI1i1Iii111 . model_id . model ] . browse ( Oo00OOOOoo0oo )
   if 80 - 80: o0oo0o * oOo0O0Ooo * II111iiii - O0 . oOo0O0Ooo % oo
  IiIi1I1 = { }
  o0o0O00oo0 ( iiI1i1Iii111 , iiI1i1Iii111 . model_id , iiI1i1Iii111 . field_ids , OO0000o , IiIi1I1 )
  if 13 - 13: iiiiIi11i . oo * iiiiIi11i + oo
  if 59 - 59: oo + i11iIiiIii + i1IIi / OoOO0ooOOoo0O
  for I11iIiI1 , ( oo0oooOo , o0OO0O0Oo ) in enumerate ( IiIi1I1 . items ( ) ) :
   if 78 - 78: oOo0O0Ooo / OoO0O00 - II11iiII - i1I1ii1II1iII * iiiiIi11i
   Ii1I11I = oo0oooOo . replace ( "." , "_" )
   oOOoo = o0OO0O0Oo [ "cols" ]
   iiIii1I = o0OO0O0Oo [ "rows" ]
   i111I11i [ "Tables" ] . append ( {
 "Name" : Ii1I11I ,
 "Cols" : oOOoo ,
 "Data" : iiIii1I ,
 } )
   if 47 - 47: Oo . OoOO0ooOOoo0O / Ooo00oOo00o
  return i111I11i
  if 83 - 83: Ooo00oOo00o / II11iiII / II11iiII + Ooo00oOo00o * o0oo0o + Ooo00oOo00o
 def _set_report_data ( self , values , report_data ) :
  if 36 - 36: oOo0O0Ooo + Ooo00oOo00o - OoooooooOO . iiiiIi11i . OoooooooOO / OoO0O00
  if 72 - 72: i1IIi
  if 82 - 82: oOo0O0Ooo + OoooooooOO / i11iIiiIii * oOoO0oo0OOOo . OoooooooOO
  oooo0OOo = [
 "var cfprint_addr = \"127.0.0.1\"" ,
 "var _delay_close = -1"
 ]
  IiII1IiiIiI1 . debug ( 'Dump report data to json...' )
  OoO00 = json . dumps ( report_data )
  if 18 - 18: o0000oOoOoO0o - OoooooooOO % II111iiii - oo % oOo0O0Ooo
  if 60 - 60: iIii1I11I1II1 + i1IIi
  IiII1IiiIiI1 . debug ( 'Encrypt report data...' )
  o0o = ii1I . rand_aes_key ( 16 , False )
  IiII1IiiIiI1 . debug ( "AES Key: %s" % ( o0o ) )
  OooOOo0 = ii1I ( o0o , AES . MODE_CBC )
  ooO000O = OooOOo0 . encrypt ( OoO00 )
  if 53 - 53: Ooo00oOo00o . i1I1ii1II1iII / o0000oOoOoO0o
  if 39 - 39: o0000oOoOoO0o % O0 % oOo0O0Ooo . i1IIi
  IiII1IiiIiI1 . debug ( 'Encrypt key...' )
  if 86 - 86: ooOO00oOo * OoooooooOO
  if 71 - 71: iIii1I11I1II1 - II11iiII . oo % OoooooooOO + II11iiII
  if 26 - 26: OoO0O00 + II11iiII / ooOO00oOo % oOo0O0Ooo % oOoO0oo0OOOo + II111iiii
  if 31 - 31: OoOO0ooOOoo0O % II11iiII * OoOO0ooOOoo0O
  OooOOo0 = ii1I ( OooO0OO ( ) , AES . MODE_CBC )
  IiI = OooOOo0 . encrypt ( o0o )
  if 34 - 34: OoOO0ooOOoo0O % Oo . O0 . iIii1I11I1II1
  ooi1II1I = {
 "token" : IiI . decode ( "utf-8" ) ,
 "dea" : "aes" ,
  "tea" : "aes" ,
  "data" : ooO000O . decode ( "utf-8" )
 }
  if 95 - 95: ooOO00oOo - II11iiII / II111iiii % oOoO0oo0OOOo . Ooo00oOo00o
  IiII1IiiIiI1 . debug ( 'Dump final_data...' )
  if 24 - 24: i1IIi . i11iIiiIii
  oooo0OOo . append ( "var _data = %s" % ( json . dumps ( ooi1II1I ) ) )
  if 16 - 16: OoO0O00 % oOoO0oo0OOOo + OoOO0ooOOoo0O - O0 . i1I1ii1II1iII / o0oo0o
  oooo0OOo . append ( """_reportData = JSON.stringify(_data);\nconsole.log(_reportData);""" )
  IIi1I = ";\n" . join ( oooo0OOo )
  IiII1IiiIiI1 . debug ( 'json_data: %s ...' % ( IIi1I [ 0 : 300 ] ) )
  if 27 - 27: O0 . o0oo0o / i1I1ii1II1iII
  values . update (
 cfprint_json = IIi1I ,
 )
  if 96 - 96: oOoO0oo0OOOo % Oo % o0000oOoOoO0o - Oo % oOo0O0Ooo + oOoO0oo0OOOo
 @ api . multi
 def render ( self , template , values = None ) :
  if values is None :
   if 3 - 3: O0
   if 64 - 64: i1IIi % Oo / i11iIiiIii - i1IIi % II11iiII . i1I1ii1II1iII
   if 8 - 8: OoO0O00 + II111iiii * II11iiII * oOo0O0Ooo * OoOO0ooOOoo0O / oooO0oo0oOOOO
   if 21 - 21: iiiiIi11i / OoooooooOO
   if 11 - 11: II11iiII % o0000oOoOoO0o - i11iIiiIii - iiiiIi11i + Oo + oooO0oo0oOOOO
   if 87 - 87: o0oo0o * i1IIi / oOoO0oo0OOOo
   values = { }
   if 6 - 6: Ooo00oOo00o + OoO0O00 - OoooooooOO % II11iiII * oOo0O0Ooo
  IiII1IiiIiI1 . debug ( "Render report..." )
  Ooo0OOoOoO0 = self . _get_report_from_name ( template )
  if not Ooo0OOoOoO0 :
   raise AccessError ( _ ( u"未找到报表（%s）定义，可能是报表未定义或定义未生效，如果使用康虎云报表，请在报表定义中重新生成一下报表定义！" % ( template ) ) )
   if 69 - 69: i1IIi
  iIII1I1i1i = oOo0O % ( _ ( u"正在打印，请稍候...<br/><br/>如果打印机未输出报表，请检查康虎云报表是否已启动！<br/><br/><a href=\"cfprint://open\">启动康虎云报表</a>" ) )
  if 59 - 59: II111iiii - Ooo00oOo00o
  IiII1IiiIiI1 . debug ( "Prepare docs..." )
  OO0000o = values . get ( "docs" , False )
  if not OO0000o or len ( OO0000o ) < 1 :
   Oo00OOOOoo0oo = self . _context . get ( "active_ids" , [ ] )
   OO0000o = self . env [ Ooo0OOoOoO0 . model ] . browse ( Oo00OOOOoo0oo )
   values . update ( docs = OO0000o )
  if not OO0000o or len ( OO0000o ) < 1 :
   iIII1I1i1i = oOo0O % ( _ ( u"没有可以打印数据。" ) )
   if 24 - 24: OoO0O00 - i1IIi + OoOO0ooOOoo0O
  IiII1IiiIiI1 . debug ( "Retrieve report define..." )
  if 38 - 38: OoooooooOO / oOoO0oo0OOOo . O0 / i1IIi / OoO0O00 + iIii1I11I1II1
  ooO00O00oOO = Ooo0OOoOoO0 . xml_id . split ( "." )
  if len ( ooO00O00oOO ) > 1 :
   ooO00O00oOO = ooO00O00oOO [ 1 ] . replace ( i1I , "" )
  else :
   ooO00O00oOO = ooO00O00oOO [ 0 ] . replace ( i1I , "" )
   if 40 - 40: i1I1ii1II1iII . iiiiIi11i + oo + oOoO0oo0OOOo + o0oo0o
  values . update (
 show_message = iIII1I1i1i
 )
  if 26 - 26: iIii1I11I1II1
  if 87 - 87: oOoO0oo0OOOo / OoooooooOO - OoO0O00 % oOo0O0Ooo % oooO0oo0oOOOO % OoO0O00
  Ii1 = self . env [ "cf.report.define" ] . search ( [ ( 'name' , '=' , ooO00O00oOO ) ] , limit = 1 )
  if 34 - 34: i1I1ii1II1iII - OoooooooOO . oo / II111iiii
  IiII1IiiIiI1 . debug ( "Prepare to make json...[%s]" % ( ooO00O00oOO ) )
  if Ii1 :
   IiII1IiiIiI1 . debug ( "Set report_define to values..." )
   values . update ( report_define = Ii1 , )
   IiII1IiiIiI1 . debug ( "Begin to make report data ..." )
   II1II = self . _make_cfprint_json ( values )
   IiII1IiiIiI1 . debug ( "Begin to convert report data to json..." )
   self . _set_report_data ( values , II1II )
   IiII1IiiIiI1 . debug ( "Converted!!!" )
   if 97 - 97: i11iIiiIii / II11iiII % o0oo0o
  ooo0 = super ( iiI1I1 , self ) . render ( template , values )
  return ooo0
  if 55 - 55: OoO0O00
 def action_upload_templ_win ( self ) :
  ooO0o = self . _context . get ( "templ_id" , False )
  return {
 'name' : _ ( u'上传康虎云报表模板' ) ,
 'type' : 'ir.actions.act_window' ,
 'view_type' : 'form' ,
 'res_model' : 'cf.template' ,
 'res_id' : ooO0o ,

  'context' : self . _context ,
 'target' : 'current' ,
 'nodestroy' : True
 }
  if 25 - 25: iIii1I11I1II1 - i1I1ii1II1iII
 @ api . model
 def render_qweb_html ( self , docids , data = None ) :
  if 3 - 3: oo * Oo + II111iiii - ooOO00oOo
  OOOO = data . get ( "is_design" , False )
  OoOO0OOoo = _ ( u"设计" ) if OOOO else _ ( u"打印" )
  if 1 - 1: oo * i11iIiiIii + o0oo0o * i11iIiiIii + ooOO00oOo
  Ii1 = self . cf_report_define_id
  if Ii1 :
   if not docids :
    docids = data . get ( "docids" , None )
    if 30 - 30: OoO0O00 . ooOO00oOo
   iIII1I1i1i = oOo0O % ( _ ( u"正在打印，请稍候...<br/><br/>如果打印机未输出报表，请检查康虎云报表是否已启动！<br/><br/><a href=\"cfprint://open\">启动康虎云报表</a>" ) )
   if 57 - 57: OoOO0ooOOoo0O . OoO0O00 + II111iiii
   OO0000o = data . get ( "docs" , False )
   if 43 - 43: o0oo0o % i1I1ii1II1iII
   if ( not OO0000o or not isinstance ( OO0000o , list ) or len ( OO0000o ) < 1 ) and docids and Ii1 and Ii1 . model_id and Ii1 . model_id . model :
    OO0000o = self . env [ Ii1 . model_id . model ] . browse ( docids )
    if 69 - 69: i1I1ii1II1iII % ooOO00oOo
   if not OO0000o or len ( OO0000o ) < 1 :
    iIII1I1i1i = oOo0O % ( _ ( u"没有可以%s数据。" ) % ( OoOO0OOoo ) )
    if 86 - 86: iiiiIi11i / iiiiIi11i
   data . update ( docs = OO0000o , show_message = iIII1I1i1i , )
   if 28 - 28: i11iIiiIii / Ooo00oOo00o . iIii1I11I1II1 / II111iiii
   if Ii1 :
    data . update ( report_define = Ii1 , )
    II1II = self . with_context ( is_design = OOOO ) . _make_cfprint_json ( data )
    self . _set_report_data ( data , II1II )
    if 72 - 72: OoooooooOO / oo + o0000oOoOoO0o / oOo0O0Ooo * o0000oOoOoO0o
  return super ( iiI1I1 , self ) . render_qweb_html ( docids , data )
  if 34 - 34: O0 * O0 % OoooooooOO + i1I1ii1II1iII * iIii1I11I1II1 % o0000oOoOoO0o
  if 25 - 25: OoOO0ooOOoo0O + oOo0O0Ooo . Ooo00oOo00o % oOo0O0Ooo * II11iiII
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
