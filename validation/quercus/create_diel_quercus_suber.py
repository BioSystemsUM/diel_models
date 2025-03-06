import cobra
import os
from diel_models.diel_models_creator import diel_models_creator


def diel_quercus(model):

    diel_models_creator(model,
                        ["C00089__cyto", "C00059__cyto", "C00244__cyto", "C00135__cyto", "C00407__cyto", "C00123__cyto",
                         "C00047__cyto", "C00073__cyto", "C02265__cyto", "C00188__cyto", "C00525__cyto", "C00183__cyto",
                         "C00062__cyto", "C00491__cyto", "C00064__cyto", "C00037__cyto", "C00148__cyto", "C00082__cyto",
                         "C01401__cyto", "C00025__cyto", "C00152__cyto", "C00065__cyto", "C00369__cyto", "C02336__cyto",
                         "C00208__cyto", "C00122__cyto", "C00158__cyto"], ["EX_C00205__dra"], ["EX_C00244__dra"], "e_Biomass_Leaf__cyto"
                        )

    cobra.io.write_sbml_model(model, os.path.join('models', 'diel_quercus_model.xml'))

def diel_quercus_wo_nitrate(model):

    diel_models_creator(model,
                        ["C00089__cyto_Leaf", "C00089__cyto_Ibark", "C00089__cyto_Phellogen",
                         "C00059__cyto_Leaf", "C00059__cyto_Ibark", "C00059__cyto_Phellogen", "C00244__cyto_Leaf",
                         "C00244__cyto_Ibark", "C00244__cyto_Phellogen", "C00135__cyto_Leaf", "C00135__cyto_Ibark",
                         "C00135__cyto_Phellogen", "C00407__cyto_Leaf", "C00407__cyto_Ibark", "C00407__cyto_Phellogen",
                         "C00123__cyto_Leaf", "C00123__cyto_Ibark", "C00123__cyto_Phellogen", "C00073__cyto_Leaf",
                         "C00073__cyto_Ibark", "C00073__cyto_Phellogen", "C02265__cyto_Leaf", "C02265__cyto_Ibark",
                         "C02265__cyto_Phellogen", "C00188__cyto_Leaf", "C00188__cyto_Ibark", "C00188__cyto_Phellogen",
                         "C00525__cyto_Leaf", "C00525__cyto_Ibark", "C00525__cyto_Phellogen", "C00183__cyto_Leaf",
                         "C00183__cyto_Ibark", "C00183__cyto_Phellogen", "C00062__cyto_Leaf", "C00062__cyto_Ibark",
                         "C00062__cyto_Phellogen", "C00491__cyto_Leaf", "C00491__cyto_Ibark", "C00491__cyto_Phellogen",
                         "C00064__cyto_Leaf", "C00064__cyto_Ibark", "C00064__cyto_Phellogen", "C00037__cyto_Leaf",
                         "C00037__cyto_Ibark", "C00037__cyto_Phellogen", "C00148__cyto_Leaf", "C00148__cyto_Ibark",
                         "C00148__cyto_Phellogen", "C00082__cyto_Leaf", "C00082__cyto_Ibark", "C00082__cyto_Phellogen",
                         "C01401__cyto_Ibark", "C01401__cyto_Phellogen", "C00025__cyto_Leaf",
                         "C00025__cyto_Ibark", "C00025__cyto_Phellogen", "C00152__cyto_Leaf", "C00152__cyto_Ibark",
                         "C00152__cyto_Phellogen", "C00065__cyto_Leaf", "C00065__cyto_Ibark", "C00065__cyto_Phellogen",
                         "C00369__cyto_Leaf", "C00369__cyto_Ibark", "C00369__cyto_Phellogen", "C02336__cyto_Leaf",
                         "C02336__cyto_Ibark", "C02336__cyto_Phellogen", "C00208__cyto_Leaf", "C00208__cyto_Ibark",
                         "C00208__cyto_Phellogen", "C00122__cyto_Leaf", "C00122__cyto_Ibark", "C00122__cyto_Phellogen",
                         "C00158__cyto_Leaf", "C00158__cyto_Ibark", "C00158__cyto_Phellogen"],
                        ["EX_C00205__dra"], biomass_reaction_id= "Total_biomass",tissues=
                        ['Leaf', 'Ibark', 'Phellogen'])

    cobra.io.write_sbml_model(model, 'diel_quercus_model_wo_nitrate.xml')


if __name__ == '__main__':
    quercus_model_path ='MultiTissueQuercusModel.xml'
    quercus_model = cobra.io.read_sbml_model(quercus_model_path)
    # diel_quercus(quercus_model)
    diel_quercus_wo_nitrate(quercus_model)