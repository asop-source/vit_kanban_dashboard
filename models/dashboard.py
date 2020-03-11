# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime

class vit_kanban_dashboard(models.Model):
	_name = 'vit.kanban.dashboard'
	_rec_name = 'company_id'



	def count_transaction(self):
		count_transaction_local = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Local'),('state', '=','confirm'),('picking_code', '=','outgoing')])
		count_transaction_export = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Export'),('state', '=','confirm'),('picking_code', '=','outgoing')])
		count_transaction_Kawasan_Berikat = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Kawasan Berikat'),('state', '=','confirm'),('picking_code', '=','outgoing')])
		count_transaction_subcon = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Subcon'),('state', '=','confirm'),('picking_code', '=','outgoing')])

		count_transaction_local_in = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Local'),('state', '=','confirm'),('picking_code', '=','incoming')])
		count_transaction_export_in = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Import'),('state', '=','confirm'),('picking_code', '=','incoming')])
		count_transaction_Kawasan_Berikat_in = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Kawasan Berikat'),('state', '=','confirm'),('picking_code', '=','incoming')])
		count_transaction_subcon_in = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Subcon'),('state', '=','confirm'),('picking_code', '=','incoming')])
		
		for obj in self:
			if obj.transaction_type == 'Local' and obj.code_picking == 'outgoing':
				obj.count_transaction_type = count_transaction_local
			elif obj.transaction_type == 'Export' and obj.code_picking == 'outgoing':
				obj.count_transaction_type = count_transaction_export
			elif obj.transaction_type == 'Kawasan Berikat' and obj.code_picking == 'outgoing':
				obj.count_transaction_type = count_transaction_Kawasan_Berikat
			elif obj.transaction_type == 'Subcon' and obj.code_picking == 'outgoing':
				obj.count_transaction_type = count_transaction_subcon

		for req in self:
			if req.transaction_type == 'Local' and req.code_picking == 'incoming':
				req.count_transaction_type = count_transaction_local_in
			elif req.transaction_type == 'Import' and req.code_picking == 'incoming':
				req.count_transaction_type = count_transaction_export_in
			elif req.transaction_type == 'Kawasan Berikat' and req.code_picking == 'incoming':
				req.count_transaction_type = count_transaction_Kawasan_Berikat_in
			elif req.transaction_type == 'Subcon' and req.code_picking == 'incoming':
				req.count_transaction_type = count_transaction_subcon_in

	def count_state(self):
		count_transaction_local_draft = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Local'),('state', '=','draft'),('date_end','>',datetime.now()),('picking_code', '=','outgoing')])
		count_transaction_export_draft = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Export'),('state', '=','draft'),('date_end','>',datetime.now()),('picking_code', '=','outgoing')])
		count_transaction_Kawasan_Berikat_draft = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Kawasan Berikat'),('state', '=','draft'),('date_end','>',datetime.now()),('picking_code', '=','outgoing')])
		count_transaction_subcon_draft = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Subcon'),('state', '=','draft'),('date_end','>',datetime.now()),('picking_code', '=','outgoing')])

		count_transaction_local_draft_in = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Local'),('state', '=','draft'),('date_end','>',datetime.now()),('picking_code', '=','incoming')])
		count_transaction_export_draft_in = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Import'),('state', '=','draft'),('date_end','>',datetime.now()),('picking_code', '=','incoming')])
		count_transaction_Kawasan_Berikat_draft_in = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Kawasan Berikat'),('state', '=','draft'),('date_end','>',datetime.now()),('picking_code', '=','incoming')])
		count_transaction_subcon_draft_in = self.env['vit.kanban'].search_count([('partner_id.transaction_type', '=','Subcon'),('state', '=','draft'),('date_end','>',datetime.now()),('picking_code', '=','incoming')])
		
		for obj in self:
			if obj.transaction_type == 'Local' and obj.code_picking == 'outgoing':
				obj.count_state_draft = count_transaction_local_draft
			elif obj.transaction_type == 'Export' and obj.code_picking == 'outgoing':
				obj.count_state_draft = count_transaction_export_draft
			elif obj.transaction_type == 'Kawasan Berikat' and obj.code_picking == 'outgoing':
				obj.count_state_draft = count_transaction_Kawasan_Berikat_draft
			elif obj.transaction_type == 'Subcon' and obj.code_picking == 'outgoing':
				obj.count_state_draft = count_transaction_subcon_draft

			if obj.transaction_type == 'Local' and obj.code_picking == 'incoming':
				obj.count_state_draft = count_transaction_local_draft_in
			elif obj.transaction_type == 'Import' and obj.code_picking == 'incoming':
				obj.count_state_draft = count_transaction_export_draft_in
			elif obj.transaction_type == 'Kawasan Berikat' and obj.code_picking == 'incoming':
				obj.count_state_draft = count_transaction_Kawasan_Berikat_draft_in
			elif obj.transaction_type == 'Subcon' and obj.code_picking == 'incoming':
				obj.count_state_draft = count_transaction_subcon_draft_in


	company_id = fields.Many2one('res.company','Company',default=lambda self: self.env.user.company_id, track_visibility='onchange')
	transaction_type = fields.Selection([
		('Local','Local'),
		('Export','Export'),
		('Import','Import'),
		('Kawasan Berikat','Kawasan Berikat'),
		('Subcon','Subcon'),
	], string="Default Transaction Type",required=True)

	code_picking = fields.Selection([('outgoing','Outgoing'),('incoming','Incoming')],string='Picking Code', track_visibility='onchange')
	count_transaction_type = fields.Integer(compute="count_transaction")
	count_state_draft = fields.Integer(compute="count_state")


	def get_action_late(self):
		if self.code_picking == 'incoming':
			return {
			'name' : _('Incoming Draft'),
			'domain' : [('partner_id.transaction_type', '=', self.transaction_type),('picking_code', '=', self.code_picking),('state', '=', 'draft')],
			'view_type' : 'form',
			'res_model' : 'vit.kanban',
			'context' : {'default_picking_code':'incoming'},
			'view_id' : False,
			'view_mode' : 'tree,form',
			'type':'ir.actions.act_window',
				}
		elif self.code_picking == 'outgoing':
			return {
			'name' : _('Outgoing Draft'),
			'domain' : [('partner_id.transaction_type', '=', self.transaction_type),('picking_code', '=', self.code_picking),('state', '=', 'draft')],
			'view_type' : 'form',
			'res_model' : 'vit.kanban',
			'context' : {'default_picking_code':'outgoing'},
			'view_id' : False,
			'view_mode' : 'tree,form',
			'type':'ir.actions.act_window',
		}



	def get_outgoing_dashboard(self):
		return {
			'name' : _(self.company_id.name),
			'domain' : [('company_id.name', '=', self.company_id.name),('picking_code', '=', self.code_picking)],
			'view_type' : 'form',
			'res_model' : 'vit.kanban',
			'view_id' : False,
			'view_mode' : 'tree,form',
			'type':'ir.actions.act_window',
		}


	def get_action_transaction_type(self):
		return {
			'name' : _(self.transaction_type),
			'domain' : [('partner_id.transaction_type', '=', self.transaction_type),('state', '=','confirm'),('picking_code', '=', self.code_picking)],
			'view_type' : 'form',
			'res_model' : 'vit.kanban',
			'view_id' : False,
			'view_mode' : 'tree,form',
			'type':'ir.actions.act_window',
		}