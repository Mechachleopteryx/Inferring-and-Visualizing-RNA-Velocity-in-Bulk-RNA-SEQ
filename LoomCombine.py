import loompy


list = ['loom1.loom', 'loom2.loom', 'loom3.loom']
loompy.combine(list, 'Combined.loom', key="Accession")