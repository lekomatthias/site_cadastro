// Função para formatar o CPF
function formatarCPFTexto(cpf) {
    cpf = cpf.replace(/\D/g, ''); // Remove tudo que não for número
    if (cpf.length === 11) {
        return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4'); // Formata o CPF
    }
    return cpf; // Retorna o CPF sem formatação se não tiver 11 dígitos
}

// Função para formatar o número de telefone
function formatarTelefoneTexto(telefone) {
    let value = telefone.replace(/\D/g, ''); // Remove tudo que não for número
    if (value.length > 13) value = value.slice(0, 13); // Limita a 13 dígitos

    if (value.length === 13) {
        // Formato com DDI: +55 (11) 9 9999-9999
        return `+${value.slice(0, 2)} (${value.slice(2, 4)}) ${value.slice(4, 5)} ${value.slice(5, 9)}-${value.slice(9, 13)}`;
    } else if (value.length === 11) {
        // Formato sem DDI: (11) 9 9999-9999
        return `(${value.slice(0, 2)}) ${value.slice(2, 3)} ${value.slice(3, 7)}-${value.slice(7, 11)}`;
    }
    return telefone; // Retorna o telefone sem formatação se não tiver 11 ou 13 dígitos
}