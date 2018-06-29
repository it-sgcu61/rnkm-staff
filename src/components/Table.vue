<template>
  <div class='container'>
    <section class='section container box'>
      <h1 class="title">RNKM staff : database
        <span style="color: red"><br>[ตัดรอบล่าสุด 29 Jun 22:30]</span>
      </h1>
      <p class='subtitle'>
        <br>เว็ปไซต์แสดงผลขอมูล staff งาน รับน้องก้าวใหม่<br>
        หากเปิดบน safari ภาพอาจจะไม่โหลด แต่สามารถเปิดผ่าน facebook หรือ line ได้<br>
        <span style='color:red'>หากลบภาพใน google-drive ภาพจะไม่แสดงผล ต้องกรอกฟอร์มใหม่</span>
      </p>
      <a href='https://goo.gl/forms/K0e9zDqoG2qfB0Z22'>กรอกข้อมูล</a><br/>
      <a href='https://docs.google.com/spreadsheets/d/1uH9ujSfsYbQSsNAev8DBHT8BPPgjuL0Q5O4faka5_bM'>ข้อมูลปัจจุบัน</a>
      <p>
        จำนวนข้อมูลปัจจุบัน : {{table.length}}
      </p>

      <div class="select">
        <select v-model='select_g["ฝ่าย"]' @change='select_g["ฝ่ายย่อย"] = ""'>
          <option v-for='g in group_list["ฝ่าย"]' :value='g'>{{g}}</option>
        </select>
      </div>
      <div class="select">
        <select v-model='select_g["ฝ่ายย่อย"]'>
          <option v-for='g in group_list["ฝ่ายย่อย"]' :value='g'>{{g}}</option>
        </select>
      </div>

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
          <tr v-for='(obj, x) in table' v-show='filt(obj)'>
            <td v-for='val in obj'>
              <div v-if='isURL(val)'>
                <img :src='val' ref='refimg'><br>
                <a style="font-size: 10px" :href='val'>link</a>
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
import _ from 'lodash'
export default {
  data() {
    return {
      table: [],
      select_g: {
        "ฝ่าย": "",
        "ฝ่ายย่อย": ""
    }}
  },
  created() {
    this.table = _.sortBy(_.values(require('../others/information.json'))
      .map(o => _.omit(o, "Timestamp")), ["ฝ่าย", "ฝ่ายย่อย"])
  },
  mounted() {
    var self = this
    for (let i in this.table){
      window.setInterval(x => {
        let it = self.$refs.refimg[x]
        if (it !== undefined && it.naturalHeight * 3 !== it.naturalWidth * 4){
          it.style['border'] = 'red solid'
        }
      }, 5000, i)
    }
  },
  methods: {
    isURL(val){
      return val.match(/^https?:/g)
    },
    filt(obj){
      let flt = this.select_g
      return _.keys(flt).every(k =>
        obj[k].indexOf(flt[k]) != -1
      )
    }
  },
  computed: {
    group_list(){
      return {
        "ฝ่าย":    [''].concat(_.uniq(_.map(this.table, "ฝ่าย"))).sort(),
        "ฝ่ายย่อย": [''].concat(_.uniq(_.map(this.table.filter(obj =>
          obj["ฝ่าย"].indexOf(this.select_g["ฝ่าย"]) != -1), "ฝ่ายย่อย"))).sort()
    }}
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
  background: url('https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif') 50% no-repeat;
}
input {
  width: 100%;
  border: none;
  text-align: center;
}
select {
  min-width: 200px;
}
</style>
