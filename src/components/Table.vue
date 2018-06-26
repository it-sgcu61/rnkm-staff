<template>
  <div class='container'>
    <section class='section container box'>
      <h1 class="title">RNKM staff : database</h1>
      <p class='subtitle'>
        เว็ปไซต์แสดงผลขอมูล staff งาน รับน้องก้าวใหม่ หากเปิดบน safari ภาพอาจจะไม่โหลด แต่สามารถเปิดผ่าน facebook หรือ line ได้
      </p>
    </section>
    <div class="container box">
      <table class="table">
        <thead>
          <tr>
            <td v-for='val in Object.keys(table[0])'>
              <strong>{{val}}</strong>
            </td>
          </tr>
        </thead>
        <tbody>
          <tr v-for='(obj, x) in table'>
            <td v-for='val in obj'>
              <div v-if='isURL(val)'>
                <img :src='val' ref='refimg' style=''>
              </div>
              <div v-else>
                <p style="margin-top: 50px">{{val}}</p>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style='height: 10px'></div>
</div>
</template>

<script>
export default {
  data() {
    return {
      table: []
    }
  },
  created() {
    this.table = Object.values(require('../others/information.json'))
    this.table.map(obj => delete obj['Timestamp'])
    var self = this
    for (let i in this.table){
      setTimeout(x => {
        let it = self.$refs.refimg[x]
        if (it.naturalHeight * 3 !== it.naturalWidth * 4){
          it.style['border'] = 'red solid'
        }
      }, 7000, i)
    }
  },
  methods: {
    isURL(val){
      return val.match(/^https?:/g)
    }
  }
}
</script>

<style scoped>
table {
  overflow: scroll;
  margin: 0px auto
}
tr td {
  text-align: center;
  font-size: 14px;
  /* white-space: nowrap; */
}
strong {
  font-size: 16px;
}
img {
  min-width: 80px;
  max-width: 100px;
}
</style>
