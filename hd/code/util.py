import frappe

from frappe import _
import json
from erpnext.controllers.queries import get_match_cond
from ast import literal_eval
from frappe.utils import (cstr, flt, cint, getdate, now_datetime, formatdate,
	strip, get_timestamp, random_string)

@frappe.whitelist(allow_guest=True)
def ping():
    return 'pong'
