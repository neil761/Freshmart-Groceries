const mongoose = require('mongoose')

const Schema = mongoose.Schema

const employSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    role: {
        type: String,
        requied: true
    },
}, {timestamps: true})

module.exports = mongoose.model('Product', employSchema)