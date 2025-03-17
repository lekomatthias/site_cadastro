// Função para formatar o CPF
function formatarCPF(campo) {
    let value = campo.value.replace(/\D/g, ''); // Remove tudo que não for número
    if (value.length > 11) value = value.slice(0, 11); // Limita a 11 dígitos
    campo.value = value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
}

// Função para formatar o número de telefone
function formatarTelefone(campo) {
    let value = campo.value.replace(/\D/g, ''); // Remove tudo que não for número
    if (value.length > 13) value = value.slice(0, 13); // Limita a 13 dígitos

    if (value.length === 13) {
        // Formato com DDI: +55 (11) 9 9999-9999
        campo.value = `+${value.slice(0, 2)} (${value.slice(2, 4)}) ${value.slice(4, 5)} ${value.slice(5, 9)}-${value.slice(9, 13)}`;
    } else if (value.length === 11) {
        // Formato sem DDI: (11) 9 9999-9999
        campo.value = `(${value.slice(0, 2)}) ${value.slice(2, 3)} ${value.slice(3, 7)}-${value.slice(7, 11)}`;
    }
}

// Função para limpar a formatação antes de enviar os dados para o servidor
function limparFormatacaoAntesDeEnviar() {
    var cpf = document.getElementById("cpf");
    var celular = document.getElementById("celular");

    // Remove a formatação
    cpf.value = cpf.value.replace(/\D/g, ''); // Remove todos os caracteres não numéricos
    celular.value = celular.value.replace(/\D/g, ''); // Remove todos os caracteres não numéricos
}

// Função de validação do formulário
function validarFormulario(event) {
    event.preventDefault(); // Impede o envio do formulário imediatamente

    let valido = true;

    // Validando o nome
    let nome = document.getElementById("nome").value;
    let errorNome = document.getElementById("errorNome");
    if (nome.trim() === "") {
        errorNome.textContent = "O nome é obrigatório.";
        document.getElementById("nome").classList.add("invalid");
        valido = false;
    } else {
        errorNome.textContent = "";
        document.getElementById("nome").classList.remove("invalid");
    }

    // Validando o CPF
    let cpf = document.getElementById("cpf").value;
    let errorCpf = document.getElementById("errorCpf");
    if (!validarCPF(cpf)) {
        errorCpf.textContent = "CPF inválido.";
        document.getElementById("cpf").classList.add("invalid");
        valido = false;
    } else {
        errorCpf.textContent = "";
        document.getElementById("cpf").classList.remove("invalid");
    }

    // Validando o e-mail
    let email = document.getElementById("email").value;
    let errorEmail = document.getElementById("errorEmail");
    if (!validarEmail(email)) {
        errorEmail.textContent = "E-mail inválido.";
        document.getElementById("email").classList.add("invalid");
        valido = false;
    } else {
        errorEmail.textContent = "";
        document.getElementById("email").classList.remove("invalid");
    }

    // Validando o celular
    let celular = document.getElementById("celular").value;
    let errorCelular = document.getElementById("errorCelular");
    if (!validarCelular(celular)) {
        errorCelular.textContent = "Número de celular inválido.";
        document.getElementById("celular").classList.add("invalid");
        valido = false;
    } else {
        errorCelular.textContent = "";
        document.getElementById("celular").classList.remove("invalid");
    }

    // Se todos os campos estiverem válidos, limpa a formatação e envia o formulário
    if (valido) {
        limparFormatacaoAntesDeEnviar();
        document.getElementById("cadastroForm").submit(); // Envia o formulário
    }
}

// Função para validar o CPF (apenas um exemplo simples, use uma validação real em produção)
function validarCPF(cpf) {
    cpf = cpf.replace(/\D/g, '');
    return cpf.length === 11;
}

// Função para validar o e-mail
function validarEmail(email) {
    const regexEmail = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    return regexEmail.test(email);
}

// Função para validar o celular
function validarCelular(celular) {
    celular = celular.replace(/\D/g, '');
    return celular.length === 11 || celular.length === 13; // Aceita 11 ou 13 dígitos
}