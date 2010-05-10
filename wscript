#!/usr/bin/env python
SUBDIRS = 'echo'

top = '.'
out = 'build'

def set_options(opt):
    opt.sub_options(SUBDIRS)

def configure(conf):
    conf.sub_config(SUBDIRS)

def build(bld):
    bld.add_subdirs(SUBDIRS)

