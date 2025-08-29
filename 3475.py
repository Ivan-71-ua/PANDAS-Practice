
import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    m_has_start = samples['dna_sequence'].str.startswith('ATG')
    m_has_stop = samples['dna_sequence'].str.endswith(('TAA', 'TAG', 'TGA'))
    m_has_atat = samples['dna_sequence'].str.contains('ATAT')
    m_has_ggg = samples['dna_sequence'].str.contains('GGG')

    samples['has_start'] = m_has_start.astype(int)
    samples['has_stop'] = m_has_stop.astype(int)
    samples['has_atat'] = m_has_atat.astype(int)
    samples['has_ggg'] = m_has_ggg.astype(int)

    return samples.sort_values("sample_id")

