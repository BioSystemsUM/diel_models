import cobra
import os
from diel_models.diel_models_creator import diel_models_creator

def diel_sugarcane(model):

    diel_models_creator(model,
                        ["S_Sucrose_c", "S_Sulfate_c", "S_Nitrate_c", "S_L_45_Histidine_c", "S_L_45_Isoleucine_c",
                         "S_L_45_Leucine_c", "S_L_45_Lysine_c", "S_L_45_Methionine_c", "S_L_45_Phenylalanine_c",
                         "S_L_45_Tryptophan_c", "S_L_45_Threonine_c", "S_L_45_Valine_c", "S_L_45_Asparagine_c",
                         "S_L_45_Cystine_c", "S_L_45_Glutamine_c", "S_Glycine_c", "S_L_45_Proline_c",
                         "S_L_45_Tyrosine_c", "S_Glutamate_c", "S_L_45_Alanine_c", "S_L_45_Aspartate_c",
                         "S_L_45_Serine_c", "S_Starch_p", "S_beta_45_D_45_Fructose_c", "S__40_S_41__45_Malate_c",
                         "S_Fumarate_c", "S_Citrate_c"], ["EX11"], ["EX_S_Nitrate_ext"])

    cobra.io.write_sbml_model(model, os.path.join('models', 'diel_sugarcane_model.xml'))


if __name__ == '__main__':
    sugarcane_model_path = os.path.join('models', 'SugarCane_C4GEM_vs1.0.xml')
    sugarcane_model = cobra.io.read_sbml_model(sugarcane_model_path)
    diel_sugarcane(sugarcane_model)
