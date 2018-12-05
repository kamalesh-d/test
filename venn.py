from matplotlib import pyplot as plt
from matplotlib_venn import venn2
plt.figure(figsize=(4,4))
v = venn2(subsets = (1, 1, 0.5), set_labels=('','', '',), set_colors=('red', 'blue', 'green'), alpha=0.8)
plt.plot(-0.5,0.2,'')
plt.text(-0.55,0.0, 'Inactive rhodopsin')
plt.text(-0.12,0.0, 'Common contacts')
plt.text(0.157,0.2, 'Unique contacts in other states:')
plt.text(0.22,0.1, 'Bathorhodopsin(1)')
plt.text(0.22,0.0, 'Lumirhodopsin(1)')
plt.text(0.22,-0.1, 'Metarhodopsin(3)')
plt.text(0.22,-0.2, 'M_Gα(3)')
plt.text(0.22,-0.3, 'M_arrestin(1)')
plt.show()