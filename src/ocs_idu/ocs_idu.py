# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia ! and modified by Andres Ignacio Baez

# This module is not general, is for IDU (Instituto de Desarrollo Urbano) customization

from osv import fields,osv

class ocs_crea_point():
    """
    IDU High Specific Requeriment for Office of Citizen Service  with Outsource partner    
    """


class ocs_contract(osv.osv):
    _name="ocs.contract"
    _columns = {
        'contract_id': fields.char('Contract Number',size=20,help="Contract Number or Serial", required=True),
        'start_date': fields.datetime('Start Date',help="When contract start", required=True),
        'end_date': fields.datetime('End Date',help="When contract ends"),
        'partner_id': fields.many2one('res.partner','Contractor',size=30,required=True),
    }
ocs_contract()

class ocs_tract(osv.osv):
    """ This class is only for IDU (Instituto Desarrollo Urbano Colombia), who need take control about claims 
    in building projects, from outsourcing  """
    _name = 'ocs.tract'
    _columns = {
        'road_id': fields.char('Road ID',size = 16,help="Road Identification Number",required=True),
        'name': fields.char('Description',size=20,required=True),
        'contract_id': fields.many2one('ocs.contract','Contractor',required=True),
    }
ocs_tract()

     
    
    
    
    
    
    