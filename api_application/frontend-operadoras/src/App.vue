<template>
  <div id="app">
    <h1 class="titulo">Busca de Operadoras de Saúde</h1>
    
    <div class="search-box">
      <input 
        v-model="termoBusca" 
        @keyup.enter="buscarOperadoras"
        placeholder="Digite nome, cidade ou UF..."
      />
      <button @click="buscarOperadoras">Buscar</button>
    </div>
    
    <div v-if="carregando" class="loading">Buscando...</div>
    
    <div v-if="mensagemErro" class="error">{{ mensagemErro }}</div>
    
    <div v-if="resultados.length > 0" class="results">
      <h2>{{ resultados.length }} resultados encontrados</h2>
      <div v-for="op in resultados" :key="op.Registro_ANS" class="card">
        <h3>{{ op.Razao_Social }}</h3>
        <p v-if="op.Nome_Fantasia"><strong>Nome Fantasia:</strong> {{ op.Nome_Fantasia }}</p>
        <p><strong>CNPJ:</strong> {{ op.CNPJ }}</p>
        <p><strong>Localização:</strong> {{ op.Cidade }}/{{ op.UF }}</p>
      </div>
    </div>
    
    <div v-if="buscaRealizada && resultados.length === 0 && !carregando" class="no-results">
      Nenhum resultado encontrado para "{{ ultimoTermoBuscado }}"
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      termoBusca: '',
      ultimoTermoBuscado: '',
      resultados: [],
      carregando: false,
      mensagemErro: '',
      buscaRealizada: false
    }
  },
  methods: {
    async buscarOperadoras() {
      if (!this.termoBusca.trim()) {
        this.resultados = [];
        this.buscaRealizada = false;
        return;
      }
      
      this.carregando = true;
      this.mensagemErro = '';
      this.buscaRealizada = true;
      this.ultimoTermoBuscado = this.termoBusca; 
      
      try {
        const response = await fetch(`http://localhost:5000/api/buscar?termo=${encodeURIComponent(this.termoBusca)}`);
        
        if (!response.ok) {
          throw new Error(`Erro HTTP: ${response.status}`);
        }
        
        const data = await response.json();
        console.log("Resposta da API:", data);
        
        if (data.error) {
          throw new Error(data.mensagem || 'Erro na busca');
        }
        
        this.resultados = data.resultados || [];
        
      } catch (error) {
        console.error("Erro na busca:", error);
        this.mensagemErro = `Erro: ${error.message}`;
        this.resultados = [];
      } finally {
        this.carregando = false;
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  margin: 0 auto;
  padding: 20px;
  height:100%;
  display: flex;
  flex-direction:column;
}

.search-box {
  display: flex;
  margin: 20px 0;
  padding: 50px;
}

.search-box input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 4px 0 0 4px;
}

.search-box button {
  padding: 10px 15px;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
}

.card {
  border: 1px solid #ddd;
  padding: 15px;
  margin-bottom: 10px;
  border-radius: 4px;
}

.loading, .no-results, .error {
  padding: 15px;
  text-align: center;
  margin: 20px 0;
}

.error {
  color: #ff4444;
}
</style>